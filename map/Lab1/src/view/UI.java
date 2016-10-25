package view;

import controller.Controller;
import exceptions.VehicleNotFoundException;
import model.Bicycle;
import model.Car;
import model.Motorcyle;
import model.Vehicle;
import org.apache.commons.lang3.ArrayUtils;

import java.util.Scanner;

/**
 * Created by cosmin on 10/7/16.
 */
public class UI {
    Controller c;
    public UI(Controller c) {
        this.c = c;
    }
    void showMenu() {
        System.out.println("Menu: ");
        System.out.println("    1. insert vehicle");
        System.out.println("    2. remove vehicle");
        System.out.println("    3. show all red vehicles");
        System.out.println("    4. exit");
    }
    private int readInteger(Scanner scanner) {
        while(!scanner.hasNextInt()) {
            scanner.next();
            System.out.println("Please input an integer");
        }
        int x = scanner.nextInt();
        scanner.nextLine();
        return x;
    }

    private String readString(Scanner scanner, String text) {
        System.out.println(text);
        return scanner.nextLine();
    }

    private double readDouble(Scanner scanner, String text) {
        System.out.println(text);
        while(!scanner.hasNextDouble()) {
            scanner.next();
            System.out.println("Please input a double");
        }
        double x = scanner.nextDouble();
        scanner.nextLine();
        return x;
    }

    private Vehicle readVehicle(Scanner scanner) {
        System.out.println("Vehicle type (Bicycle, Car, Motorcycle)");
        String vehicleType;
        do {
            vehicleType = scanner.nextLine();
        } while(!ArrayUtils.contains(new String[]{"bicycle", "car", "motorcycle"}, vehicleType.toLowerCase()));
        String type, color, brand, name;
        double size, maxSpeed;
        switch(vehicleType.toLowerCase()) {
            case "bicycle":
                type = readString(scanner, "Type: ");
                color = readString(scanner, "Color: ");
                size = readDouble(scanner, "Wheel Size: ");
                return new Bicycle(type, color, size);
            case "car":
                type = readString(scanner, "Type: ");
                brand = readString(scanner, "Brand: ");
                name = readString(scanner, "Name: ");
                color = readString(scanner, "Color: ");
                return new Car(type, brand, name, color);
            case "motorcycle":
                brand = readString(scanner, "Brand: ");
                name = readString(scanner, "Name: ");
                color = readString(scanner, "Color: ");
                maxSpeed = readDouble(scanner, "Max Speed: ");
                return new Motorcyle(brand, name, color, maxSpeed);
        }
        return null;
    }

    public void run() {
        Scanner scanner = new Scanner(System.in);
        while(true) {
            showMenu();
            int x = readInteger(scanner);
            Vehicle v;
            switch(x) {
                case 1:
                    System.out.println("1");
                    v = readVehicle(scanner);
                    System.out.println(v.toString());
                    this.c.add(v);
                    break;
                case 2:
                    System.out.println("2");
                    v = readVehicle(scanner);
                    System.out.println(v.toString());
                    try {
                        this.c.remove(v);
                    } catch(VehicleNotFoundException e) {
                        System.out.println("The following exception occurred: " + e.getMessage());
                    }
                    break;
                case 3:
                    System.out.println("3");
                    Vehicle[] arr = c.solve();
                    System.out.println(arr.length);
                    for(Vehicle veh : arr)
                        System.out.println(veh.toString());
                    break;
                case 4:
                    System.out.println("Bye bye!");
                    return ;
            }
        }
    }
}
