package model;

import org.apache.commons.lang3.builder.ToStringBuilder;

/**
 * Created by cosmin on 10/24/16.
 */
public class PrgState {
    private MyIStack <IStmt> exeStack;
    private MyIDictionary <String, Integer> symTable;
    private MyIList<Integer> out;
    private IStmt originalProgram;
    public PrgState(MyIStack<IStmt> exeStack, MyIDictionary<String, Integer> symTable, MyIList<Integer> out, IStmt prg) {
        this.exeStack = exeStack;
        this.symTable = symTable;
        this.out = out;
        this.originalProgram = prg;
        this.exeStack.push(prg);
    }
    public MyIStack<IStmt> getExeStack() {
        return this.exeStack;
    }
    public MyIDictionary<String, Integer> getSymTable() {
        return this.symTable;
    }
    public MyIList<Integer> getOut() {
        return this.out;
    }
    @Override
    public String toString() {
        ToStringBuilder builder = new ToStringBuilder(this)
                .append(exeStack.toString())
                .append(symTable.toString())
                .append(out.toString());
        return builder.build();
    }
}
