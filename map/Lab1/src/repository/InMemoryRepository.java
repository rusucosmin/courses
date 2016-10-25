package repository;

import exceptions.VehicleNotFoundException;
import model.Vehicle;

/**
 * Created by cosmin on 10/7/16.
 */
public class InMemoryRepository implements Repository {
    int cap;
    int size;
    Vehicle[] arr;

    public InMemoryRepository() {
        cap = 2;
        size = 0;
        arr = new Vehicle[2];
    }

    public InMemoryRepository(Vehicle[] arr) {
        this.arr = arr;
        this.size = arr.length;
        this.cap = (int) Math.ceil(Math.pow(2, Math.ceil(Math.log(this.size))));
    }

    @Override
    public void add(Vehicle v) {
        arr[size] = v;
        ++size;
        if (size == cap) {
            cap *= 2;
            Vehicle[] newArr = new Vehicle[cap];
            for (int i = 0; i < size; ++i) {
                newArr[i] = arr[i];
            }
            arr = newArr;
        }
    }

    @Override
    public boolean find(Vehicle v) {
        for(int i = 0; i < size; ++ i)
            if(arr[i].equals(v))
                return true;
        return false;
    }

    @Override
    public void remove(Vehicle v) throws VehicleNotFoundException {
        Vehicle[] filter = new Vehicle[cap];
        int actSize = 0;
        for (int i = 0; i < size; ++i)
            if (!arr[i].equals(v)) {
                filter[actSize++] = arr[i];
            }
        if(actSize == size) {
            throw new VehicleNotFoundException();
        }
        size = actSize;
        arr = filter;
    }

    @Override
    public Vehicle[] getAll() {
        return arr;
    }
}
