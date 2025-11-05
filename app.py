from flask import Flask, request, jsonify

app = Flask(__name__)


dispositivos = {
    1: {"nombre": "Router01", "descripcion": "Router principal", "caracteristicas": "Cisco, 4 puertos LAN"},
    2: {"nombre": "Switch01", "descripcion": "Switch secundario", "caracteristicas": "TP-Link, 8 puertos"}
}


@app.route('/')
def listar_dispositivos():
    html = """
    <h2>Listado de Dispositivos de Red</h2>
    <table border="1" cellpadding="5" cellspacing="0">
        <thead>
            <tr>
                <th>ID</th>
                <th>Nombre</th>
                <th>Descripción</th>
                <th>Características</th>
            </tr>
        </thead>
        <tbody>
    """
    for id, info in dispositivos.items():
        html += f"""
        <tr>
            <td>{id}</td>
            <td>{info['nombre']}</td>
            <td>{info['descripcion']}</td>
            <td>{info['caracteristicas']}</td>
        </tr>
        """
    html += "</tbody></table>"
    return html


@app.route('/agregar', methods=['POST'])
def agregar_dispositivo():
    data = request.get_json()
    nuevo_id = max(dispositivos.keys()) + 1 if dispositivos else 1
    dispositivos[nuevo_id] = {
        "nombre": data.get("nombre"),
        "descripcion": data.get("descripcion"),
        "caracteristicas": data.get("caracteristicas")
    }
    return jsonify({"mensaje": "Dispositivo agregado exitosamente", "id": nuevo_id}), 201

@app.route('/modificar/<int:id>', methods=['PUT'])
def modificar_dispositivo(id):
    if id not in dispositivos:
        return jsonify({"error": "Dispositivo no encontrado"}), 404
    data = request.get_json()
    dispositivos[id].update({
        "nombre": data.get("nombre", dispositivos[id]["nombre"]),
        "descripcion": data.get("descripcion", dispositivos[id]["descripcion"]),
        "caracteristicas": data.get("caracteristicas", dispositivos[id]["caracteristicas"])
    })
    return jsonify({"mensaje": "Dispositivo modificado correctamente"}), 200

if __name__ == '__main__':
    app.run(debug=True)
