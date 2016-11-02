package exception;

/**
 * Created by cosmin on 02/11/16.
 */
public class FileNotOpenedException extends Exception {
    public FileNotOpenedException() {
        super("FileNotOpenedException");
    }
    public FileNotOpenedException(String s) {
        super(s);
    }
}
