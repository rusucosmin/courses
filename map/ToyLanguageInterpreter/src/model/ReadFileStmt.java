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
public class ReadFileStmt implements IStmt {
    private Exp exp;
    private String var;

    public ReadFileStmt(Exp exp, String var) {
        this.exp = exp;
        this.var = var;
    }

    @Override
    public PrgState execute(PrgState state) throws IOException, FileAlreadyOpenedException, FileNotOpenedException, UnknownVariableException, DivideByZeroException {
        int fd = this.exp.eval(state.getSymTable(), state.getHeap());
        Tuple<String, BufferedReader> br = state.getFileTable().get(fd);
        if (br == null)
            throw new FileNotOpenedException("FileNotOpenedException at: " + this.toString() + "\nNo such file descriptor: " + String.valueOf(fd));
        String line = br.getSecond().readLine();
        int val = 0;
        if(line != null)
            val = Integer.valueOf(line);
        state.getSymTable().put(this.var, val);
        return state;
    }

    @Override
    public String toString() {
        return "readFileStmt (" + this.exp.toString() + ", " + this.var + ")";
    }
}
