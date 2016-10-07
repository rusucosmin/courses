package controller;

import model.Vehicle;
import repository.Repository;

/**
 * Created by cosmin on 10/7/16.
 */
public class Controller {
    Repository r;
    public Controller(Repository r) {
        this.r = r;
    }
    public void add(Vehicle v) {
        this.r.add(v);
    }
    public void remove(Vehicle v) {
        this.r.remove(v);
    }
    public Vehicle[] solve() {
        int cnt = 0;
        for(Vehicle v : this.r.getAll())
            if(v != null && v.getColor().equals("red")) {
                ++ cnt;
            }
        Vehicle[] arr = new Vehicle[cnt];
        cnt = 0;
        for(Vehicle v: this.r.getAll())
            if(v != null && v.getColor().equals("red"))
                arr[cnt ++] = v;
        return arr;
    }
}
