package model;

import java.io.Serializable;
import java.util.HashMap;
import java.util.Map;

/**
 * Created by cosmin on 11/11/16.
 */
public class MyHeap<T> implements MyIHeap <T> {
    int memory;
    Map<Integer, T> vals;
    public MyHeap(Map<Integer, T> vals) {
        this.vals = vals;
    }
    @Override
    public int allocate(T value) {
        ++ this.memory;
        this.vals.put(this.memory, value);
        return memory;
    }

    @Override
    public T readAddr(int addr) {
        return this.vals.get(addr);
    }

    @Override
    public void writeAddr(int addr, T value) {
        this.vals.put(addr, value);
    }

    @Override
    public T deallocate(int addr) {
        return this.vals.remove(addr);
    }

    @Override
    public String toString() {
        String ret = "";
        boolean ok = false;
        for(HashMap.Entry<Integer, T> entry : this.vals.entrySet()) {
            if(ok)
                ret = ret + "\n";
            ret += entry.getKey().toString() + " -> " + entry.getValue().toString();
            ok = true;
        }
        return ret;
    }

    @Override
    public void setMap(Map<Integer, T> map) {
        this.vals = map;
    }

    @Override
    public Map<Integer, T> getMap() {
        return this.vals;
    }
}
