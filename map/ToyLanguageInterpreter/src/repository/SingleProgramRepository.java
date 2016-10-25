package repository;

import model.PrgState;

/**
 * Created by cosmin on 10/25/16.
 */
public class SingleProgramRepository implements IRepository {
    private PrgState state;
    public SingleProgramRepository(PrgState state) {
        this.state = state;
    }
    @Override
    public PrgState getCrtState() {
        return this.state;
    }
}
