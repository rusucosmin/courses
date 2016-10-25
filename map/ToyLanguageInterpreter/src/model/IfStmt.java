package model;

/**
 * Created by cosmin on 10/25/16.
 */
public class IfStmt implements IStmt {
    private Exp exp;
    private IStmt thenS;
    private IStmt elseS;

    public IfStmt(Exp exp, IStmt thenS, IStmt elseS) {
        this.exp = exp;
        this.thenS = thenS;
        this.elseS = elseS;
    }

    @Override
    public String toStr() {
        return "If " + exp.toStr() + " then " + thenS.toStr() + " else " + elseS.toStr();
    }

    @Override
    public PrgState execute(PrgState state) {
        if(exp.eval(state.getSymTable()) == 0)
            state.getExeStack().push(elseS);
        else
            state.getExeStack().push(thenS);
        return state;
    }
}
