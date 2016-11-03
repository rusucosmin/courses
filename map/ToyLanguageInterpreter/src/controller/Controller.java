package controller;

import exception.DivideByZeroException;
import exception.FileAlreadyOpenedException;
import exception.FileNotOpenedException;
import exception.UnknownVariableException;
import model.IStmt;
import model.PrgState;
import repository.IRepository;

import java.io.IOException;

/**
 * Created by cosmin on 10/25/16.
 */
public class Controller {
    IRepository rep;
    public Controller(IRepository rep) {
        this.rep = rep;
    }

    public PrgState oneStep(PrgState state) throws UnknownVariableException, DivideByZeroException, FileAlreadyOpenedException, FileNotOpenedException, IOException {
        IStmt cur = state.getExeStack().pop();
        return cur.execute(state);
    }

    public void allSteps() throws UnknownVariableException, DivideByZeroException, FileAlreadyOpenedException, FileNotOpenedException, IOException {
        PrgState crt = rep.getCrtState();
        while(!crt.getExeStack().isEmpty()) {
            oneStep(crt);
            try {
                rep.logPrgStateExec();
            } catch (IOException e) {
                System.out.println("Cannot log program state to file. Exiting...");
                return ;
            }
        }
    }
}
