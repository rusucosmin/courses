package model;

import exception.KeyNotExistException;

import java.util.Collection;

/**
 * Created by cosmin on 10/24/16.
 */
public interface MyIDictionary <K, V> {
    V put(K key, V value);
    V get(K key) ;
    Collection<V> values();
    V remove(K fd);
}
