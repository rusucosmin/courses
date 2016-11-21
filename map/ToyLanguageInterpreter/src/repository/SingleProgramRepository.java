package repository;

import model.PrgState;

import java.io.*;

/**
 * Created by cosmin on 10/25/16.
 */
public class SingleProgramRepository implements IRepository {
    private String logFile;
    private PrgState state;
    private PrintWriter printWriter;
    private boolean firstTime;
    public SingleProgramRepository(PrgState state, String logFile) {
        this.state = state;
        this.logFile = logFile;
        this.printWriter = null;
        this.firstTime = true;
    }
    public void setMain(PrgState state) {
        this.state = state;
    }
    @Override
    public PrgState getCrtState() {
        return this.state;
    }

    @Override
    public void logPrgStateExec() throws IOException {
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

        this.printWriter.println("ExeStack:");
        this.printWriter.println(this.state.getExeStack().toString());
        this.printWriter.println("SymTable:");
        this.printWriter.println(this.state.getSymTable().toString());
        this.printWriter.println("Out:");
        this.printWriter.println(this.state.getOut().toString());
        this.printWriter.println("FileTable:");
        this.printWriter.println(this.state.getFileTable().toString());
        this.printWriter.println("Heap:");
        this.printWriter.println(this.state.getHeap().toString());

        this.printWriter.close();
    }

    @Override
    public void serialize() {
        ObjectOutputStream out = null;
        try {
            out = new ObjectOutputStream(new FileOutputStream("serialize.txt"));
            out.writeObject(this.state);
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
            state = (PrgState) in.readObject();
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
        if(state != null) {
            this.state = state;
        }
    }
}
