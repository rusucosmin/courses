package model;

/**
 * Created by cosmin on 10/25/16.
 */
public class ConstExp extends Exp {
    public int value;

    public ConstExp(int value) {
        this.value = value;
    }

    @Override
    public int eval(MyIDictionary<String, Integer> symTable) {
        return value;
    }

    @Override
    public String toStr() {
        return String.valueOf(value);
    }
}
