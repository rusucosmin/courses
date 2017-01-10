package model;

import exception.DivideByZeroException;
import exception.FileAlreadyOpenedException;
import exception.FileNotOpenedException;
import exception.UnknownVariableException;

import java.io.IOException;

/**
 * Created by cosmin on 11/11/16.
 */
public class ReadHeapExp extends Exp  {
    String id;
    public ReadHeapExp(String id) {
        this.id = id;
    }

    @Override
    public int eval(MyIDictionary<String, Integer> symTable, MyIHeap<Integer> heap) throws UnknownVariableException, UnknownVariableException, DivideByZeroException, NullPointerException {
        Integer var_val = symTable.get(this.id);
        if(var_val == null)
            throw new UnknownVariableException("Unknown variable exception\nError at ReadHeapExp: " + toString());
        Integer heap_val = heap.readAddr(var_val);
        if(heap_val == null)
            throw new NullPointerException("There is no such memory address\nError at ReadHeapExp: " + toString());
        return heap_val;
    }

    @Override
    public String toString() {
        return "readHeapExp(" + id + ")";
    }
}
