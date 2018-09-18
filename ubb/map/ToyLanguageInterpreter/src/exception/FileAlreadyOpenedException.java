package exception;

/**
 * Created by cosmin on 02/11/16.
 */
public class FileAlreadyOpenedException extends Exception {
    public FileAlreadyOpenedException() {
        super("FileAlreadyOpenedException");
    }
    public FileAlreadyOpenedException(String s) {
        super(s);
    }
}
