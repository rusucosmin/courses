package model;

/**
 * Created by cosmin on 10/24/16.
 */
public abstract class Exp {
    abstract public int eval(MyIDictionary<String, Integer> symTable);
    abstract public String toStr();
}
