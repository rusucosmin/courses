package model;

/**
 * Created by cosmin on 02/11/16.
 */
public class Tuple <T1, T2> {
    private T1 t1;
    private T2 t2;
    public Tuple(T1 t1, T2 t2) {
        this.t1 = t1;
        this.t2 = t2;
    }
    public T1 getFirst() {
        return t1;
    }
    public T2 getSecond() {
        return t2;
    }
    @Override
    public String toString() {
        return this.t1.toString();
    }
}
