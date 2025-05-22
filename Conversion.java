import java.util.Scanner;

public class Conversion {
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        float Jeringascoin = 595.55f;
        int opcion;
        String salida;

        do {
            System.out.println("Menu de opciones");
            System.out.println("1. Convertir de pesos a Jeringascoin");
            System.out.println("2. Convertir de Jeringascoin a pesos");
            opcion = scanner.nextInt();

            switch (opcion) {
                case 1:
                    System.out.println("Ingrese la cantidad de pesos a convertir:");
                    float pesos = scanner.nextFloat();
                    float jeringascoin = pesos / Jeringascoin;
                    System.out.println(pesos + " pesos son " + jeringascoin + " Jeringascoin");
                    break;
                case 2:
                    System.out.println("Ingrese la cantidad de Jeringascoin a convertir:");
                    float jeringascoin2 = scanner.nextFloat();
                    float pesosConvertidos = jeringascoin2 * Jeringascoin;
                    System.out.println(jeringascoin2 + " Jeringascoin son " + pesosConvertidos + " pesos");
                    break;
                default:
                    System.out.println("Opcion no valida");
            }

            System.out.println("¿Desea salir del programa? (escriba 'si' para salir):");
            salida = scanner.next();
        } while (!salida.equalsIgnoreCase("si"));
    }
}
