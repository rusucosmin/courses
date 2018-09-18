package model;

import exception.DivideByZeroException;
import exception.UnknownComparisonExpression;
import exception.UnknownVariableException;

/**
 * Created by cosmin on 1/26/17.
 */
public class NotExp extends Exp {
    private Exp exp;
    public NotExp(Exp exp) {
        this.exp = exp;
    }
    @Override
    public int eval(MyIDictionary<String, Integer> symTable, MyIHeap<Integer> heap) throws DivideByZeroException, UnknownVariableException, UnknownComparisonExpression {
        // if x evals to 0 => false => !false = true
        /// else !true = false
        int x = this.exp.eval(symTable, heap);
        if(x == 0)
            return 1;
        return 0;
    }

    @Override
    public String toString() {
        return "!" + this.exp.toString();
    }
}
