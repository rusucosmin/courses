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
import java.util.List;
import java.util.Map;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutorService;
import java.util.stream.Collector;
import java.util.stream.Collectors;

/**
 * Created by cosmin on 10/25/16.
 */
public class Controller {
    IRepository rep;
    private ExecutorService executor;
    public Controller(IRepository rep) {
        this.rep = rep;
    }

    Map<Integer, Integer> conservativeGarbageCollector(Collection<Integer> symTableValues, Map<Integer, Integer> heap) {
        return heap.entrySet()
                .stream()
                .filter(e->symTableValues.contains(e.getKey()))
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
    }

    public List<PrgState> removeCompletedPrg(List<PrgState> prgStateList) {
        return prgStateList.stream()
                .filter(p -> p.isNotCompleted())
                .collect(Collectors.toList());
    }

    public void setMain(PrgState state) {
        this.rep.setMain(state);
    }

    void serialize() {
        this.rep.serialize();;
    }

    public void allStepsForAllPrg(List<PrgState> prgList) throws InterruptedException {
        /// Log the states before the execution
        prgList.forEach(prg -> rep.logPrgStateExec(prg));

        List<Callable<PrgState>> callList = prgList.stream()
                .map((PrgState p) -> (Callable<PrgState>)(() -> {return p.oneStep();}))
                .collect(Collectors.toList());

        List<PrgState> newPrgList = executor.invokeAll(callList).stream()
                .map(future -> {
                    try {
                        return future.get();
                    } catch (Exception e) {
                        System.out.println(e);
                    }
                    return null;
                })
                .filter(p -> p != null)
                .collect(Collectors.toList());

        prgList.addAll(newPrgList);
        prgList.forEach(prg -> {
            try {
                rep.logPrgStateExec(prg);
            } catch (IOException e) {
                e.printStackTrace();
            }
        });

        rep.setPrgList(prgList);
    }

    public void allSteps() throws UnknownVariableException, DivideByZeroException, FileAlreadyOpenedException, FileNotOpenedException, IOException, UnknownComparisonExpression {
        List<PrgState> prgList = rep.getPrgList();
        while(!crt.getExeStack().isEmpty()) {
            //this.rep.serialize();
            oneStep(crt);
            crt.getHeap().setMap(this.conservativeGarbageCollector(crt.getSymTable().values(), crt.getHeap().getMap()));
            //this.rep.deserialize();
            try {
                rep.logPrgStateExec();
            } catch (IOException e) {
                System.out.println("Cannot log program state to file. Exiting...");
                return ;
            }
        }
    }
}
