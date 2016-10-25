import model.*;
import controller.*;
import repository.*;

import java.util.*;

/**
 * Created by cosmin on 10/25/16.
 */
public class Main {
    public static void main(String [] args) {
        MyIStack<IStmt> exeStack = new MyStack<>(new Stack<IStmt>());
        MyIDictionary<String, Integer> symTable = new MyDictionary<>(new HashMap<String, Integer>());
        MyIList<Integer> out = new MyList<>(new ArrayList<Integer>());
        IStmt ex1= new CompStmt(new AssignStmt("v",new ConstExp(2)), new PrintStmt(new
                VarExp("v")));
        // a=2+3*5;b=a+1;Print(b)
        IStmt ex2 = new CompStmt(new AssignStmt("a", new ArithExp('+',new ConstExp(2),new
                ArithExp('*',new ConstExp(3), new ConstExp(5)))),
                new CompStmt(new AssignStmt("b",new ArithExp('+',new VarExp("a"), new
                        ConstExp(1))), new PrintStmt(new VarExp("b"))));
        // a=2-2;
        //(If a Then v=2 Else v=3);
        //Print(v)
        IStmt ex3 = new CompStmt(new AssignStmt("a", new ArithExp('-',new ConstExp(2), new
                ConstExp(2))),
                new CompStmt(new IfStmt(new VarExp("a"),new AssignStmt("v",new ConstExp(2)), new
                        AssignStmt("v", new ConstExp(3))), new PrintStmt(new VarExp("v"))));
        PrgState prgState = new PrgState(exeStack, symTable, out, ex3);
        IRepository repo = new SingleProgramRepository(prgState);
        Controller ctrl = new Controller(repo);
        ctrl.allSteps();
    }
}
