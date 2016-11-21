package model;

import controller.Controller;
import exception.*;

import javax.naming.ldap.Control;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;
import java.util.Stack;

/**
 * Created by cosmin on 11/21/16.
 */
public class InputProgramCommand extends Command {

    private static final int STATEMENT_COMPOUND = 1;
    private static final int STATEMENT_ASSIGNMENT = 2;
    private static final int STATEMENT_PRINT = 3;
    private static final int STATEMENT_IF = 4;
    private static final int STATEMENT_WHILE = 5;
    private static final int STATEMENT_NEW_HEAP = 6;
    private static final int STATEMENT_OPEN_R_FILE = 7;
    private static final int STATEMENT_READ_FILE = 8;
    private static final int STATEMENT_CLOSE_FILE = 9;

    private static final int EXPRESSION_CONSTANT = 1;
    private static final int EXPRESSION_VARIABLE = 2;
    private static final int EXPRESSION_ARITH = 3;
    private static final int EXPRESSION_COMP = 4;
    private static final int EXPRESSION_READ_HEAP = 5;

    private static Scanner keyboard = new Scanner(System.in);
    Controller ctrl;
    public InputProgramCommand(String id, String descr, Controller ctrl) {
        super(id, descr);
        this.ctrl = ctrl;
    }

    @Override
    public void execute(){
        IStmt prg = getStatement();
        MyIStack<IStmt> exeStack = new MyStack<>(new Stack<IStmt>());
        MyIDictionary<String, Integer> symTable = new MyDictionary<>(new HashMap<String, Integer>());
        MyIList<Integer> out = new MyList<>(new ArrayList<Integer>());
        MyIDictionary<Integer, Tuple<String, BufferedReader>> fileTable = new MyDictionary<>(new HashMap<Integer, Tuple<String, BufferedReader>>());
        MyIHeap<Integer> heap = new MyHeap<Integer>(new HashMap<Integer, Integer>());

        PrgState prgState = new PrgState(exeStack, symTable, out, prg, fileTable, heap);
        this.ctrl.setMain(prgState);
        try {
            this.ctrl.allSteps();
        } catch (UnknownVariableException e) {
            e.printStackTrace();
        } catch (DivideByZeroException e) {
            e.printStackTrace();
        } catch (FileAlreadyOpenedException e) {
            e.printStackTrace();
        } catch (FileNotOpenedException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } catch (UnknownComparisonExpression unknownComparisonExpression) {
            unknownComparisonExpression.printStackTrace();
        }
    }

    public static int getInt(String ask) {
        String s = getString(ask);
        try {
            return Integer.parseInt(s);
        } catch (NumberFormatException e) {
            System.out.println("ERROR: the input is not an integer. Try again...");
            return getInt(ask);
        }
    }

    public static String getString(String ask) {
        String line = null;
        while(line == null) {
            System.out.println(ask);
            line = keyboard.nextLine().trim();
            if(line.isEmpty())
                line = null;
        }
        return line;
    }

    private int getCommand(String from) {
        return getInt(String.format("(%s)> ", from));
    }

    private char getArithmeticOperator() {
        printArithmeticOperatorMenu();
        while(true) {
            int x = getInt("operator = ");
            switch(x) {
                case ArithExp.ADD:
                    return '+';
                case ArithExp.DIVIDE:
                    return '/';
                case ArithExp.MULTIPLY:
                    return '*';
                case ArithExp.SUBTRACT:
                    return '-';
                default:
                    System.out.println("ERROR: operator is not valid!");
            }
        }
    }

    private void printArithmeticOperatorMenu() {
        String out = "";

        out += "Choose arithmetic operation:\n";
        out += String.format("%d. Add\n", ArithExp.ADD);
        out += String.format("%d. Subtract\n", ArithExp.SUBTRACT);
        out += String.format("%d. Multiply\n", ArithExp.MULTIPLY);
        out += String.format("%d. Divide\n", ArithExp.DIVIDE);

        System.out.println(out);
    }

    private void printCompOperatorMenu() {
        String out = "";

        out += "Choose compare opertator:\n";
        out += String.format("%d. <\n", CompExp.LESS_THAN);
        out += String.format("%d. <=\n", CompExp.LESS_THAN_OR_EQUAL);
        out += String.format("%d. ==\n", CompExp.EQUAL);
        out += String.format("%d. !=\n", CompExp.NOT_EQUAL);
        out += String.format("%d. >\n", CompExp.GREATER_THAN);
        out += String.format("%d. >=\n", CompExp.GREATER_THAN_OR_EQUAL);

        System.out.println(out);
    }

    private void printExpressionMenu() {
        String out = "";

        out += "Choose expression type:\n";
        out += String.format("%d. Constant Expression\n", EXPRESSION_CONSTANT);
        out += String.format("%d. Variable Expression\n", EXPRESSION_VARIABLE);
        out += String.format("%d. Arithmetic Expression\n", EXPRESSION_ARITH);
        out += String.format("%d. Compare Expression\n", EXPRESSION_COMP);
        out += String.format("%d. Read Heap Expression\n", EXPRESSION_READ_HEAP);

        System.out.println(out);
    }

    private String getCompOperator() {
        printCompOperatorMenu();
        while(true) {
            int x = getInt("operator = ");
            switch(x) {
                case CompExp.LESS_THAN:
                    return "<";
                case CompExp.EQUAL:
                    return "==";
                case CompExp.GREATER_THAN:
                    return ">";
                case CompExp.NOT_EQUAL:
                    return "!=";
                case CompExp.GREATER_THAN_OR_EQUAL:
                    return ">=";
                case CompExp.LESS_THAN_OR_EQUAL:
                    return "<=";
            }
        }
    }

    private Exp getExpression() {
        printExpressionMenu();
        switch(getCommand("expression")) {
            case EXPRESSION_CONSTANT:
                System.out.println("Constant(<integer>)");
                return new ConstExp(getInt("const value = "));
            case EXPRESSION_VARIABLE:
                System.out.println("Variable Expression (<var>)");
                return new VarExp(getString("var name = "));
            case EXPRESSION_ARITH:
                System.out.println("ArithExp(<expression>, < + | - | * | / >, <expression>");
                Exp earith1 = getExpression();
                char x = getArithmeticOperator();
                Exp earith2 = getExpression();
                return new ArithExp(x, earith1, earith2);
            case EXPRESSION_COMP:
                System.out.println("Compare(<expression>, > | < | <= | >= | == | != , <expression>");
                Exp ecomp1 = getExpression();
                String type = getCompOperator();
                Exp ecomp2 = getExpression();
                return new CompExp(type, ecomp1, ecomp2);

            case EXPRESSION_READ_HEAP:
                System.out.println("readHeap(<var_name>)");
                return new ReadHeapExp(getString("var name = "));

            default:
                System.out.println("ERROR: Expression not recognized!");
        }
        return null;
    }

    public void printStatementMenu() {
        String out = "Please choose a statement type:\n";

        out += String.format("%d. Compound Statement\n", STATEMENT_COMPOUND);
        out += String.format("%d. Assignment Statement\n", STATEMENT_ASSIGNMENT);
        out += String.format("%d. If Statement\n", STATEMENT_IF);
        out += String.format("%d. Print Statement\n", STATEMENT_PRINT);
        out += String.format("%d. While Statement\n", STATEMENT_WHILE);
        out += String.format("%d. New Heap Statement\n", STATEMENT_NEW_HEAP);
        out += String.format("%d. Open File Statement\n", STATEMENT_OPEN_R_FILE);
        out += String.format("%d. Read File Statement\n", STATEMENT_READ_FILE);
        out += String.format("%d. Close File Statement\n", STATEMENT_CLOSE_FILE);

        System.out.println(out);
    }

    private IStmt getStatement() {
        printStatementMenu();
        switch(getCommand("statement")) {
            case STATEMENT_COMPOUND:
                System.out.println("CompStmt(<statement>, <statement>)");

                return new CompStmt(getStatement(), getStatement());
            case STATEMENT_ASSIGNMENT:
                System.out.println("<var> = <expression>)");

                return new AssignStmt(getString("var name = "), getExpression());

            case STATEMENT_IF:
                System.out.println("If(<expression>); then <statement>; else <statement>");

                return new IfStmt(getExpression(), getStatement(), getStatement());

            case STATEMENT_PRINT:
                System.out.println("Print(<expression>)");

                return new PrintStmt(getExpression());

            case STATEMENT_WHILE:
                System.out.println("While(<expression>) <statement>");

                return new WhileStmt(getExpression(), getStatement());

            case STATEMENT_NEW_HEAP:
                System.out.println("new (<variable>, <expression>)");

                return new NewStmt(getString("var name = "), getExpression());

            case STATEMENT_OPEN_R_FILE:
                System.out.println("new (<variable>, <FileName>)");
                return new OpenRFileStmt(getString("var name = "), getString("file name = "));

            case STATEMENT_READ_FILE:
                System.out.println("read (<expression>, <variable>)");
                return new ReadFileStmt(getExpression(), getString("var name = "));

            case STATEMENT_CLOSE_FILE:
                System.out.println("close_file(<expression>)");
                return new CloseRFileStmt(getExpression());

            default:
                System.out.println("ERROR: Statement not recognized!");
        }
        return null;
    }
}
