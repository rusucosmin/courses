package model;

import exception.DivideByZeroException;
import exception.UnknownComparisonExpression;
import exception.UnknownVariableException;

/**
 * Created by cosmin on 10/24/16.
 */
public class PrintStmt implements IStmt {
    private Exp exp;

    public PrintStmt(Exp exp) {
        this.exp = exp;
    }

    @Override
    public String toString() {
        return "print (" + exp + ")";
    }

    @Override
    public PrgState execute(PrgState state) throws UnknownVariableException, DivideByZeroException, UnknownComparisonExpression {
        MyIList <Integer> out = state.getOut();
        out.add(exp.eval(state.getSymTable(), state.getHeap()));
        return state;
    }
}
