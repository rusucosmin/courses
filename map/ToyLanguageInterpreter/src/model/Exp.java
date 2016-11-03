package model;

import exception.DivideByZeroException;
import exception.UnknownVariableException;

/**
 * Created by cosmin on 10/24/16.
 */
public abstract class Exp {
    abstract public int eval(MyIDictionary<String, Integer> symTable) throws UnknownVariableException, UnknownVariableException, DivideByZeroException;
    @Override
    abstract public String toString();
}
