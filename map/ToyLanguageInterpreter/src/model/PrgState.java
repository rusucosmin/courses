package model;

import exception.*;
import org.apache.commons.lang3.builder.ToStringBuilder;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.Serializable;

/**
 * Created by cosmin on 10/24/16.
 */
public class PrgState implements Serializable {
    private int id;
    private MyIStack <IStmt> exeStack;
    private MyIDictionary <String, Integer> symTable;
    private MyIList<Integer> out;
    private IStmt originalProgram;
    private MyIDictionary<Integer, Tuple<String, BufferedReader>> fileTable;
    private MyIHeap<Integer> heap;
    private MyILatchTable latchTable;
    public PrgState(MyIStack<IStmt> exeStack, MyIDictionary<String, Integer> symTable, MyIList<Integer> out, IStmt prg, MyIDictionary<Integer, Tuple<String, BufferedReader>> fileTable, MyIHeap<Integer> heap, int id, MyILatchTable latchTable) {
        this.exeStack = exeStack;
        this.symTable = symTable;
        this.out = out;
        this.originalProgram = prg;
        this.exeStack.push(prg);
        this.fileTable = fileTable;
        this.heap = heap;
        this.id = id;
        this.latchTable = latchTable;
    }
    public int getId() {
        return id;
    }
    public void setId(int id) {
        this.id = id;
    }
    public boolean isNotCompleted() {
        return this.exeStack.isEmpty() == false;
    }
    public PrgState oneStep() throws UnknownVariableException, DivideByZeroException, FileAlreadyOpenedException, FileNotOpenedException, IOException, UnknownComparisonExpression {
        IStmt cur = this.getExeStack().pop();
        return cur.execute(this);
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
    public MyIHeap<Integer> getHeap() {
        return this.heap;
    }
    @Override
    public String toString() {
        ToStringBuilder builder = new ToStringBuilder(this)
                .append(exeStack.toString())
                .append(symTable.toString())
                .append(out.toString())
                .append(fileTable.toString())
                .append(heap.toString());
        return builder.build();
    }

    public MyILatchTable getLatchTable() {
        return latchTable;
    }
}
