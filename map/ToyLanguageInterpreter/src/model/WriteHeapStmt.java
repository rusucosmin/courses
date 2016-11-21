package model;

import exception.*;

import java.io.IOException;

/**
 * Created by cosmin on 11/11/16.
 */
public class WriteHeapStmt implements IStmt {
    String id;
    Exp exp;
    public WriteHeapStmt(String id, Exp exp) {
        this.id = id;
        this.exp = exp;
    }
    @Override
    public PrgState execute(PrgState state) throws IOException, FileAlreadyOpenedException, FileNotOpenedException, UnknownVariableException, DivideByZeroException, UnknownComparisonExpression {
        Integer var_val = state.getSymTable().get(id);
        if(var_val == null)
            throw new UnknownVariableException("Unknown variable expression\nError at: " + toString());
        int val = this.exp.eval(state.getSymTable(), state.getHeap());
        state.getHeap().writeAddr(var_val, val);
        return state;
    }

    @Override
    public String toString() {
        return "WriteHeap (" + this.id + ", " + this.exp.toString();
    }
}
