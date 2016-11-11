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
    public int eval(MyIDictionary<String, Integer> symTable, MyIHeap<Integer> heap) {
        return value;
    }

    @Override
    public String toString() {
        return String.valueOf(value);
    }
}
