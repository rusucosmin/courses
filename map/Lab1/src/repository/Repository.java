package repository;

import exceptions.VehicleNotFoundException;
import model.Vehicle;

/**
 * Created by cosmin on 10/7/16.
 */
public interface Repository {
    void add(Vehicle v);
    void remove(Vehicle v) throws VehicleNotFoundException;
    boolean find(Vehicle v);
    Vehicle [] getAll();
}
