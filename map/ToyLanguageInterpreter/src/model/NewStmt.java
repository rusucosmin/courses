package model;

import exception.DivideByZeroException;
import exception.FileAlreadyOpenedException;
import exception.FileNotOpenedException;
import exception.UnknownVariableException;

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
    public PrgState execute(PrgState state) throws IOException, FileAlreadyOpenedException, FileNotOpenedException, UnknownVariableException, DivideByZeroException {
        int res = this.exp.eval(state.getSymTable(), state.getHeap());
        int loc = state.getHeap().allocate(res);
        state.getSymTable().put(var, loc);
        return state;
    }

    @Override
    public String toString() {
        return "NewStmt (" + this.var + ", " + this.exp.toString() + " )";
    }
}
