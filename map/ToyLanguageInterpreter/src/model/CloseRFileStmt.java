package model;

import exception.DivideByZeroException;
import exception.FileAlreadyOpenedException;
import exception.FileNotOpenedException;
import exception.UnknownVariableException;

import java.io.BufferedReader;
import java.io.IOException;

/**
 * Created by cosmin on 02/11/16.
 */
public class CloseRFileStmt implements IStmt {
    private Exp exp;
    public CloseRFileStmt(Exp exp) {
        this.exp = exp;
    }

    @Override
    public String toString() {
        return "closeRFileStmt (" + this.exp.toString() + ")";
    }

    @Override
    public PrgState execute(PrgState state) throws IOException, FileAlreadyOpenedException, FileNotOpenedException, UnknownVariableException, DivideByZeroException {
        int fd = this.exp.eval(state.getSymTable());
        Tuple<String, BufferedReader> act = state.getFileTable().remove(fd);
        if(act == null)
            throw new FileNotOpenedException("FileNotOpened Exception at: " + this.toString() + "\nThere is no opened file with fd = " + fd);
        act.getSecond().close();
        return state;
    }
}
