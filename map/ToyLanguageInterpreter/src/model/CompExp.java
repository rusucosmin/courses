package model;

import exception.DivideByZeroException;
import exception.UnknownComparisonExpression;
import exception.UnknownVariableException;

/**
 * Created by cosmin on 11/15/16.
 */
public class CompExp extends Exp {
    public static final int LESS_THAN = 1;
    public static final int LESS_THAN_OR_EQUAL = 2;
    public static final int EQUAL = 3;
    public static final int NOT_EQUAL = 4;
    public static final int GREATER_THAN = 5;
    public static final int GREATER_THAN_OR_EQUAL = 6;
    private String type;
    private Exp e1, e2;
    public CompExp(String type, Exp e1, Exp e2) {
        this.type = type;
        this.e1 = e1;
        this.e2 = e2;
    }
    @Override
    public int eval(MyIDictionary<String, Integer> symTable, MyIHeap<Integer> heap) throws UnknownComparisonExpression, UnknownVariableException, UnknownVariableException, DivideByZeroException {
        int val1 = this.e1.eval(symTable, heap);
        int val2 = this.e2.eval(symTable, heap);
        switch (this.type) {
            case "<":
                return val1 < val2 ? 1 : 0;
            case "<=":
                return val1 <= val2 ? 1 : 0;
            case "==":
                return val1 == val2 ? 1 : 0;
             case "!=":
                return val1 != val2 ? 1 : 0;
            case ">":
                return val1 > val2 ? 1 : 0;
            case ">=":
                return val1 >= val2 ? 1 : 0;
            default:
                throw new UnknownComparisonExpression("Unknown comparison exception: " + this.type + "\n" + "At: " + this.toString());
        }
    }

    @Override
    public String toString() {
        return this.e1.toString() + " " +  this.type + " " + this.e2.toString();
    }
}
