package model;

import exception.FileAlreadyOpenedException;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;

/**
 * Created by cosmin on 02/11/16.
 */
public class OpenRFileStmt implements IStmt {
    private static int fd = 2; /// ARROGANCE! Because I can.
    private String id, fileName;
    public OpenRFileStmt(String id, String fileName) {
        this.id = id;
        this.fileName = fileName;
    }
    @Override
    public PrgState execute(PrgState state) throws FileNotFoundException, FileAlreadyOpenedException {
        for(Tuple<String, BufferedReader> act : state.getFileTable().values())
            if(act.getFirst() == this.fileName)
                throw new FileAlreadyOpenedException("FileAlreadyOpenedException at: " + this.toString() + "\nThe file " + this.fileName + " is already open");

        int actFd = ++ OpenRFileStmt.fd; /// static variable
        state.getFileTable().put(actFd, new Tuple<String, BufferedReader> (this.fileName, new BufferedReader(new FileReader(this.fileName))));
        state.getSymTable().put(this.id, actFd);
        return state;
    }
    @Override
    public String toString() {
        return "openRFile (" + this.id + ", " + this.fileName + ")";
    }
}
