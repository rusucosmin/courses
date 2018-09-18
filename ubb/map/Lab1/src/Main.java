import controller.Controller;
import model.Bicycle;
import model.Car;
import model.Motorcyle;
import repository.InMemoryRepository;
import repository.Repository;
import view.UI;

public class Main {

    public static void main(String[] args) {
        System.out.println("Welcome to your Garaje!");
        Repository r = new InMemoryRepository();
        r.add(new Car("SUV", "BMW", "X1", "red"));
        r.add(new Car("MCV", "Dacia", "Logan MCV", "green"));
        r.add(new Car("Sedan", "Tesla", "Model S", "red"));
        r.add(new Bicycle("bmx", "red", 12.5));
        r.add(new Bicycle("mountain-bike", "red", 15));
        r.add(new Motorcyle("Yamaha", "MotorX", "red", 345));
        Controller c = new Controller(r);
        UI ui = new UI(c);
        ui.run();
    }
}
