package model;

import exception.UnknownVariableException;

import java.util.HashMap;

/**
 * Created by cosmin on 10/24/16.
 */
public class MyDictionary <K, V> implements MyIDictionary<K, V> {
    private HashMap<K, V> _map;

    public MyDictionary(HashMap<K, V> _map) {
        this._map = _map;
    }

    @Override
    public V put(K key, V value) {
        return this._map.put(key, value);
    }

    @Override
    public V get(K key) throws UnknownVariableException {
        return this._map.get(key);
    }

    @Override
    public String toString() {
        return this._map.toString();
    }
}
