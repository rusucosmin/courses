package model;

import java.io.Serializable;
import java.util.Map;

/**
 * Created by cosmin on 11/11/16.
 */
public interface MyIHeap <T> extends Serializable {
    int allocate(T value);
    T readAddr(int addr);
    void writeAddr(int addr, T value);
    T deallocate(int addr);

    void setMap(Map<Integer, T> map);
    Map<Integer, T> toMap();
}
