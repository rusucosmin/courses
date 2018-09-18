package model;

import exception.DivideByZeroException;
import exception.UnknownComparisonExpression;
import exception.UnknownVariableException;

import java.io.Serializable;

/**
 * Created by cosmin on 10/24/16.
 */
public abstract class Exp implements Serializable {
    abstract public int eval(MyIDictionary<String, Integer> symTable, MyIHeap<Integer> heap) throws DivideByZeroException, UnknownVariableException, UnknownComparisonExpression;
    @Override
    abstract public String toString();
}
