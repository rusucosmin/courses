package model;

import exception.*;

import java.io.IOException;

/**
 * Created by cosmin on 1/26/17.
 */
public class AwaitStmt implements IStmt {
    private String var;
    public AwaitStmt(String var) {
        this.var = var;
    }
    @Override
    public PrgState execute(PrgState state) throws IOException, FileAlreadyOpenedException, FileNotOpenedException, UnknownVariableException, DivideByZeroException, UnknownComparisonExpression, IOException, UnknownComparisonExpression {
        if(state.getSymTable().get(var) == null)
            throw new UnknownVariableException("Nu exista variabila " + this.var + "\nError in AwaitStmt!");
        int index = state.getSymTable().get(var);
        Integer count = null;
        synchronized (state.getLatchTable()) {
            if (state.getLatchTable().get(index) == null)
                throw new UnknownVariableException("Nu exista latch with index: " + index + "\nError in AwaitStmt!");
            count = state.getLatchTable().get(index);
            if(count > 0)
                state.getExeStack().push(this);
        }
        return null;
    }
    @Override
    public String toString() {
        return "await(" + this.var + ")";
    }
}
