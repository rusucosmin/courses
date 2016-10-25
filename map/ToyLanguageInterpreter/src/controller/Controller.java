package controller;

import model.IStmt;
import model.PrgState;
import repository.IRepository;

/**
 * Created by cosmin on 10/25/16.
 */
public class Controller {
    IRepository rep;
    public Controller(IRepository rep) {
        this.rep = rep;
    }

    public PrgState oneStep(PrgState state) {
        IStmt cur = state.getExeStack().pop();
        return cur.execute(state);
    }

    public void allSteps() {
        PrgState crt = rep.getCrtState();
        while(!crt.getExeStack().isEmpty()) {
            oneStep(crt);
            System.out.println(crt.toString());
        }
    }
}
