package model;

import exception.UnknownVariableException;

import java.util.HashMap;

/**
 * Created by cosmin on 10/24/16.
 */
public interface MyIDictionary <K, V> {
    V put(K key, V value);
    V get(K key) throws UnknownVariableException, UnknownVariableException;
}
