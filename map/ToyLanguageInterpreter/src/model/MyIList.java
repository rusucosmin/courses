package model;

import java.io.Serializable;

/**
 * Created by cosmin on 10/24/16.
 */
public interface MyIList <T> extends Serializable {
    void add(T el);
    T get(int index);
    boolean remove(T el);
    T remove(int index);
    int size();
}
