package model;

import java.util.Collection;
import java.util.HashMap;
import java.util.Map;

/**
 * Created by cosmin on 1/26/17.
 */
public class MyLatchTable implements MyILatchTable {
    private HashMap<Integer, Integer> _map;
    public MyLatchTable(HashMap<Integer, Integer> _map) {
        this._map = _map;
    }
    @Override
    public Integer put(Integer key, Integer value) {
        return this._map.put(key, value);
    }

    @Override
    public Integer get(Integer key) {
        return this._map.get(key);
    }

    @Override
    public Collection<Integer> values() {
        return this._map.values();
    }

    @Override
    public Collection<Integer> keys() {
        return this._map.keySet();
    }

    @Override
    public Integer remove(Integer fd) {
        return _map.remove(fd);
    }

    @Override
    public MyILatchTable clone() {
        MyILatchTable dict = new MyLatchTable(new HashMap<Integer, Integer>());
        for(Integer key : _map.keySet())
            dict.put(key, _map.get(key));
        return dict;
    }

    @Override
    public Map<Integer, Integer> toMap() {
        return _map;
    }

    @Override
    public String toString() {
        String ret = "";
        boolean ok = false;
        for(HashMap.Entry<Integer, Integer> entry : this._map.entrySet()) {
            if(ok)
                ret = ret + "\n";
            ret += entry.getKey().toString() + " -> " + entry.getValue().toString();
            ok = true;
        }
        return ret;
    }
}
