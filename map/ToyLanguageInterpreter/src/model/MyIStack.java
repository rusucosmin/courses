package model;

import java.util.Stack;

/**
 * Created by cosmin on 10/24/16.
 */
public interface MyIStack <T> {
    void push(T el);
    T pop();
    T peek();
    boolean isEmpty();
}
