package utils;

/**
 * Created by cosmin on 1/2/17.
 */
public interface Observer <T> {
    void update(Observable<T> observable);
}
