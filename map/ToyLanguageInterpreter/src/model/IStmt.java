package model;

import exception.DivideByZeroException;
import exception.FileAlreadyOpenedException;
import exception.FileNotOpenedException;
import exception.UnknownVariableException;

import java.io.IOException;

/**
 * Created by cosmin on 10/24/16.
 */
public interface IStmt {
    @Override
    String toString();
    PrgState execute(PrgState state) throws IOException, FileAlreadyOpenedException, FileNotOpenedException, UnknownVariableException, DivideByZeroException;
}
