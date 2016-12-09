package repository;

import model.PrgState;
import java.io.IOException;
import java.util.List;

/**
 * Created by cosmin on 10/25/16.
 */
public interface IRepository {
    List<PrgState> getPrgList();
    void logPrgStateExec(PrgState state) throws IOException;
    void setPrgList(List<PrgState> prgList);
 //   void serialize();
 //   void deserialize();
}
