package model;

/**
 * Created by cosmin on 10/24/16.
 */
public class CompStmt implements IStmt {
    private IStmt first, second;

    public CompStmt(IStmt first, IStmt second) {
        this.first = first;
        this.second = second;
    }

    @Override
    public String toString() {
        return first.toString() + "; " + second.toString();
    }

    @Override
    public PrgState execute(PrgState state) {
        MyIStack<IStmt> stack = state.getExeStack();
        stack.push(second);
        stack.push(first);
        return null;
    }
}
