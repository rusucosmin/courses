package model;

/**
 * Created by cosmin on 10/25/16.
 */
public class ArithExp extends Exp {
    private Exp e1, e2;
    private int op;
    public ArithExp(char op, Exp e1, Exp e2) {
        this.e1 = e1;
        this.e2 = e2;
        if(op == '+')
            this.op = 0;
        else if(op == '-')
            this.op = 1;
        else if(op == '*')
            this.op = 2;
        else if(op == '/')
            this.op = 3;
    }

    @Override
    public int eval(MyIDictionary<String, Integer> symTable) {
        int rez = 0;
        int rez1 = this.e1.eval(symTable);
        int rez2 = this.e2.eval(symTable);
        if(op == 0) {
            rez = rez1 + rez2;
        } else if(op == 1) {
            rez = rez1 - rez2;
        } else if(op == 2) {
            rez = rez1 * rez2;
        } else if(op == 3) {
            rez = rez / rez2;
        }
        return rez;
    }

    @Override
    public String toStr() {
        String ret = this.e1.toString();
        if(op == 0)
            ret += " + ";
        else if(op == 1)
            ret += " - ";
        else if(op == 2)
            ret += " * ";
        else if(op == 3)
            ret += " / ";
        ret += this.e2.toString();
        return ret;
    }
}
