package repository;

import model.PrgState;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

/**
 * Created by cosmin on 10/25/16.
 */
public class Repository implements IRepository {
    private String logFile;
    private List<PrgState> prgList;
    private PrintWriter printWriter;
    private boolean firstTime;
    public Repository(PrgState state, String logFile) {
        this.prgList = new ArrayList<>();
        this.prgList.add(state);
        this.logFile = logFile;
        this.printWriter = null;
        this.firstTime = true;
    }
    @Override
    public List<PrgState> getPrgList() {
        return this.prgList;
    }

    @Override
    public void setPrgList(List<PrgState> prgList) {
        this.prgList = prgList;
    }

    @Override
    public void logPrgStateExec(PrgState state) throws IOException {
        if(firstTime == true) {
            /// first, clear the content
            try {
                PrintWriter writer = new PrintWriter(new File(logFile));
                writer.print("");
                writer.close();
            } catch (FileNotFoundException e) {
                e.printStackTrace();
            }
            firstTime = false;
        }

        this.printWriter = new PrintWriter(new FileWriter(logFile, true));

        this.printWriter.println("Thread ID: " + state.getId());
        this.printWriter.println("ExeStack:");
        this.printWriter.println(state.getExeStack().toString());
        this.printWriter.println("SymTable:");
        this.printWriter.println(state.getSymTable().toString());
        this.printWriter.println("Out:");
        this.printWriter.println(state.getOut().toString());
        this.printWriter.println("FileTable:");
        this.printWriter.println(state.getFileTable().toString());
        this.printWriter.println("Heap:");
        this.printWriter.println(state.getHeap().toString());

        this.printWriter.close();
    }

    @Override
    public void serialize() {
        ObjectOutputStream out = null;
        try {
            out = new ObjectOutputStream(new FileOutputStream("serialize.txt"));
            out.write(prgList.size());
            for(PrgState t : prgList)
                out.writeObject(t);
        } catch (IOException e) {
            System.out.println("IOError\nError: " + e.toString());
        } finally {
            if(out != null) {
                try {
                    out.close();
                } catch(IOException e) {
                    System.out.println("IOError\nError: " + e.toString());
                }
            }
        }
    }

    @Override
    public void deserialize() {
        ObjectInputStream in = null;
        PrgState state = null;
        try {
            in = new ObjectInputStream(new FileInputStream("serialize.txt"));
            int size = in.read();
            prgList.clear();
            for(int i = 0; i < size; ++ i)
                prgList.add((PrgState) in.readObject());
        } catch(IOException e) {
            System.out.println("IOError\nError: " + e.toString());
        } catch(ClassNotFoundException e) {
            System.out.println("ClassNotFoundException\nError: " + e.toString());
        }
        finally {
            if(in != null) {
                try {
                    in.close();
                } catch(IOException e) {
                    System.out.println("IOError\nError: " + e.toString());
                }
            }
        }
    }
}
