package services;

import model.PrgState;
import model.Tuple;
import repository.IRepository;
import utils.Observer;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Created by cosmin on 1/2/17.
 */
public class PrgStateService implements utils.Observable<PrgState> {
    protected List<Observer<PrgState>> observers = new ArrayList<Observer<PrgState>>();
    private IRepository repo;

    public PrgStateService(IRepository repo) {
        this.repo = repo;
    }

    public IRepository getRepo() {
        return this.repo;
    }

    public List<PrgState> getAll() {
        List<PrgState> mList = new ArrayList<PrgState>();
        mList.addAll(this.repo.getPrgList());
        return mList;
    }

    public List<String> getOutList() {
        List<String> mList = new ArrayList<String>();
        for(int i = 0; i < this.repo.getPrgList().get(0).getOut().size(); ++ i)
            mList.add(String.valueOf(this.repo.getPrgList().get(0).getOut().get(i)));
        return mList;
    }

    public List<Tuple<Integer, String>> getFileList() {
        List<Tuple<Integer, String>> mList = new ArrayList<>();
        for(Integer x : this.repo.getPrgList().get(0).getFileTable().keys())
            mList.add(new Tuple(x, this.repo.getPrgList().get(0).getFileTable().get(x).getFirst()));
        return mList;
    }

    public List<Map.Entry<Integer, Integer>> getHeapList() {
        System.out.println(repo.getPrgList().get(0).getHeap().toMap().entrySet());
        return new ArrayList<Map.Entry<Integer, Integer>>(repo.getPrgList().get(0).getHeap().toMap().entrySet());
    }

    @Override
    public void addObserver(Observer<PrgState> o) {
        observers.add(o);
    }

    @Override
    public void removeObserver(Observer<PrgState> o) {
        observers.remove(o);
    }

    @Override
    public void notifyObservers() {
        for(Observer o : observers)
            o.update(this);
    }
}
