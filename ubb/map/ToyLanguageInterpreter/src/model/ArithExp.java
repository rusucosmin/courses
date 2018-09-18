package model;

import exception.DivideByZeroException;
import exception.UnknownComparisonExpression;
import exception.UnknownVariableException;

/**
 * Created by cosmin on 10/25/16.
 */
public class ArithExp extends Exp {
    public static final int ADD = 1;
    public static final int SUBTRACT = 2;
    public static final int MULTIPLY = 3;
    public static final int DIVIDE = 4;
    private Exp e1, e2;
    private int op;
    public ArithExp(char op, Exp e1, Exp e2) {
        this.e1 = e1;
        this.e2 = e2;
        if(op == '+')
            this.op = ADD;
        else if(op == '-')
            this.op = SUBTRACT;
        else if(op == '*')
            this.op = MULTIPLY;
        else if(op == '/')
            this.op = DIVIDE;
    }

    @Override
    public int eval(MyIDictionary<String, Integer> symTable, MyIHeap<Integer> heap) throws UnknownVariableException, DivideByZeroException, UnknownComparisonExpression {
        int rez = 0;
        int rez1 = this.e1.eval(symTable, heap);
        int rez2 = this.e2.eval(symTable, heap);
        if(op == ADD) {
            rez = rez1 + rez2;
        } else if(op == SUBTRACT) {
            rez = rez1 - rez2;
        } else if(op == MULTIPLY) {
            rez = rez1 * rez2;
        } else if(op == DIVIDE) {
            if(rez2 == 0)
                throw new DivideByZeroException("DivideByZeroException at: " + this.toString());
            rez = rez / rez2;
        }
        return rez;
    }

    @Override
    public String toString() {
        String ret = this.e1.toString();
        if(op == ADD)
            ret += " + ";
        else if(op == SUBTRACT)
            ret += " - ";
        else if(op == MULTIPLY)
            ret += " * ";
        else if(op == DIVIDE)
            ret += " / ";
        ret += this.e2.toString();
        return ret;
    }
}
