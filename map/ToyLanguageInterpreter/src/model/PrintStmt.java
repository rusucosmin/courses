package model;

/**
 * Created by cosmin on 10/24/16.
 */
public class PrintStmt implements IStmt {
    private Exp exp;

    public PrintStmt(Exp exp) {
        this.exp = exp;
    }

    @Override
    public String toStr() {
        return "Print (" + exp + ")";
    }

    @Override
    public PrgState execute(PrgState state) {
        MyIList <Integer> out = state.getOut();
        out.add(exp.eval(state.getSymTable()));
        return state;
    }
}
