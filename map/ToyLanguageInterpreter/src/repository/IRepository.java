package repository;

import model.PrgState;

import java.io.IOException;

/**
 * Created by cosmin on 10/25/16.
 */
public interface IRepository {
    PrgState getCrtState();
    void logPrgStateExec() throws IOException;
    void setMain(PrgState main);
    void serialize();
    void deserialize();
}
