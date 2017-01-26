package model;

import exception.*;

import java.io.IOException;

/**
 * Created by cosmin on 1/26/17.
 */
public class RepeatStmt implements IStmt {
    private IStmt stmt;
    private Exp exp;
    public RepeatStmt(IStmt stmt, Exp exp) {
        this.stmt = stmt;
        this.exp = exp;
    }
    @Override
    public PrgState execute(PrgState state) throws IOException, FileAlreadyOpenedException, FileNotOpenedException, UnknownVariableException, DivideByZeroException, UnknownComparisonExpression, IOException, UnknownComparisonExpression {
        IStmt act = new CompStmt(stmt, new WhileStmt(new NotExp(this.exp), stmt));
        state.getExeStack().push(act);
        return null;
    }

    @Override
    public String toString() {
        return "repeat " + this.stmt.toString() + " until " + this.exp.toString();
    }
}
