package model;

import exception.*;

import java.io.IOException;

/**
 * Created by cosmin on 1/26/17.
 */
public class CountDownStmt implements IStmt {
    private String var;
    public CountDownStmt(String var) {
        this.var = var;
    }
    @Override
    public PrgState execute(PrgState state) throws IOException, FileAlreadyOpenedException, FileNotOpenedException, UnknownVariableException, DivideByZeroException, UnknownComparisonExpression, IOException, UnknownComparisonExpression {
        if(state.getSymTable().get(this.var) == null)
            throw new UnknownVariableException("Nu exista variabila " + this.var + "\nError in CountDownStmt");
        int index = state.getSymTable().get(this.var);
        synchronized (state.getLatchTable()) {
            if (state.getLatchTable().get(index) == null)
                return null; // do nothing
            int count = state.getLatchTable().get(index);
            if (count > 0) {
                state.getLatchTable().put(index, count - 1);
                state.getOut().add(state.getId());
            }
        }
        return null;
    }

    @Override
    public String toString() {
        return "countDown(" + this.var + ")";
    }
}
