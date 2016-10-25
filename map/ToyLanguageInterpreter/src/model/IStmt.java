package model;

/**
 * Created by cosmin on 10/24/16.
 */
public interface IStmt {
    String toStr();
    PrgState execute(PrgState state);
}
