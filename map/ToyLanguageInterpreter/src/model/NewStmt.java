package model;

import exception.*;

import java.io.IOException;

/**
 * Created by cosmin on 11/11/16.
 */
public class NewStmt implements IStmt {
    private String var;
    private Exp exp;
    public NewStmt(String var, Exp exp) {
        this.var = var;
        this.exp = exp;
    }
    @Override
    public PrgState execute(PrgState state) throws IOException, FileAlreadyOpenedException, FileNotOpenedException, UnknownVariableException, DivideByZeroException, UnknownComparisonExpression {
        int res = this.exp.eval(state.getSymTable(), state.getHeap());
        int loc = state.getHeap().allocate(res);
        state.getSymTable().put(var, loc);
        return null;
    }

    @Override
    public String toString() {
        return "NewStmt (" + this.var + ", " + this.exp.toString() + " )";
    }
}
