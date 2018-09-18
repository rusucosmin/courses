package model;

import exception.*;

import java.io.IOException;

/**
 * Created by cosmin on 1/26/17.
 */
public class NewLatchStmt implements IStmt {
    private static int newFreeLocation = -1;
    private String var;
    private Exp exp;
    public NewLatchStmt(String var, Exp exp) {
        this.var = var;
        this.exp = exp;
    }
    @Override
    public PrgState execute(PrgState state) throws IOException, FileAlreadyOpenedException, FileNotOpenedException, UnknownVariableException, DivideByZeroException, UnknownComparisonExpression, IOException, UnknownComparisonExpression {
        int number = this.exp.eval(state.getSymTable(), state.getHeap());
        synchronized (state.getLatchTable()) {
            ++ newFreeLocation;
            state.getLatchTable().put(newFreeLocation, number);
            state.getSymTable().put(this.var, newFreeLocation);
        }
        return null;
    }

    @Override
    public String toString() {
        return "newLatch(" + this.var + ", " + this.exp.toString() + ")";
    }
}
