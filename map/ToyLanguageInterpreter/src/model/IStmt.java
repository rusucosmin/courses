package model;

import exception.*;

import java.io.IOException;
import java.io.Serializable;

/**
 * Created by cosmin on 10/24/16.
 */
public interface IStmt extends Serializable {
    @Override
    String toString();
    PrgState execute(PrgState state) throws IOException, FileAlreadyOpenedException, FileNotOpenedException, UnknownVariableException, DivideByZeroException, UnknownComparisonExpression, IOException, UnknownComparisonExpression;
}
