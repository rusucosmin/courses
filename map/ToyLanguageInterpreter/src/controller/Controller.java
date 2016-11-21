package controller;

import exception.*;
import model.IStmt;
import model.MyIDictionary;
import model.MyIHeap;
import model.PrgState;
import repository.IRepository;

import java.io.IOException;
import java.util.Collection;
import java.util.HashMap;
import java.util.Map;
import java.util.stream.Collectors;

/**
 * Created by cosmin on 10/25/16.
 */
public class Controller {
    IRepository rep;
    public Controller(IRepository rep) {
        this.rep = rep;
    }

    Map<Integer, Integer> conservativeGarbageCollector(Collection<Integer> symTableValues, Map<Integer, Integer> heap) {
        return heap.entrySet()
                .stream()
                .filter(e->symTableValues.contains(e.getKey()))
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));

    }

    public PrgState oneStep(PrgState state) throws UnknownVariableException, DivideByZeroException, FileAlreadyOpenedException, FileNotOpenedException, IOException, UnknownComparisonExpression {
        IStmt cur = state.getExeStack().pop();
        return cur.execute(state);
    }

    public void setMain(PrgState state) {
        this.rep.setMain(state);
    }

    void serialize() {
        this.rep.serialize();;
    }

    public void allSteps() throws UnknownVariableException, DivideByZeroException, FileAlreadyOpenedException, FileNotOpenedException, IOException, UnknownComparisonExpression {
        PrgState crt = rep.getCrtState();
        while(!crt.getExeStack().isEmpty()) {
            oneStep(crt);
            crt.getHeap().setMap(this.conservativeGarbageCollector(crt.getSymTable().values(), crt.getHeap().getMap()));
            try {
                rep.logPrgStateExec();
            } catch (IOException e) {
                System.out.println("Cannot log program state to file. Exiting...");
                return ;
            }
        }
    }
}
