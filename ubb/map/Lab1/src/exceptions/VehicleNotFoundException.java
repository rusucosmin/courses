package exceptions;

/**
 * Created by cosmin on 10/14/16.
 */
public class VehicleNotFoundException extends Exception {
    public VehicleNotFoundException() {
        super("Vehicle was not found!");
    }
    public VehicleNotFoundException(String s) {
        super(s);
    }
}
