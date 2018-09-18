package utils;

/**
 * Created by cosmin on 1/2/17.
 */
public interface Observable<T> {
    void addObserver(Observer<T> o);
    void removeObserver(Observer<T> o);
    void notifyObservers();
}
