package model;

import exception.*;

import java.io.IOException;
import java.util.HashMap;
import java.util.Stack;

/**
 * Created by cosmin on 12/9/16.
 */
public class ForkStmt implements IStmt {
    private IStmt stmt;
    public ForkStmt(IStmt stmt) {
        this.stmt = stmt;
    }
    @Override
    public PrgState execute(PrgState state) throws IOException, FileAlreadyOpenedException, FileNotOpenedException, UnknownVariableException, DivideByZeroException, UnknownComparisonExpression, IOException, UnknownComparisonExpression {
        PrgState forkProgram = new PrgState(new MyStack<>(new Stack<>()), state.getSymTable().clone(), state.getOut(), this.stmt, state.getFileTable(), state.getHeap(), state.getId() * 10);
        return forkProgram;
    }
}
