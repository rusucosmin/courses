package model;

import org.apache.commons.lang3.builder.ToStringBuilder;

import java.io.BufferedReader;

/**
 * Created by cosmin on 10/24/16.
 */
public class PrgState {
    private MyIStack <IStmt> exeStack;
    private MyIDictionary <String, Integer> symTable;
    private MyIList<Integer> out;
    private IStmt originalProgram;
    private MyIDictionary<Integer, Tuple<String, BufferedReader>> fileTable;
    public PrgState(MyIStack<IStmt> exeStack, MyIDictionary<String, Integer> symTable, MyIList<Integer> out, IStmt prg, MyIDictionary<Integer, Tuple<String, BufferedReader>> fileTable) {
        this.exeStack = exeStack;
        this.symTable = symTable;
        this.out = out;
        this.originalProgram = prg;
        this.exeStack.push(prg);
        this.fileTable = fileTable;
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
    public MyIDictionary<Integer, Tuple<String, BufferedReader>> getFileTable() {
        return this.fileTable;
    }
    @Override
    public String toString() {
        ToStringBuilder builder = new ToStringBuilder(this)
                .append(exeStack.toString())
                .append(symTable.toString())
                .append(out.toString())
                .append(fileTable.toString());
        return builder.build();
    }
}
