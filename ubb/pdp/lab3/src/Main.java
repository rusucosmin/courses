import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.concurrent.*;

public class Main {
  static int[] TP = {1, 3, 10, 30, 100, 300, 1000, 3000};
  static int[] T = {1, 3, 10, 30, 100, 300, 1000, 3000};
  static String[] adds = {"add.in", "add1.in", "add2.in", "add3.in"};
  static String[] mults = {"mult.in", "mult2.in", "mult3.in", "mult4.in", "mult5.in"};
  static int n, m;

  public static double solve(String filename, int threadPoolSize,
                             int T, boolean debug, MatrixOperaterFactory<Callable<Void>> matrixOperaterFactory)
      throws FileNotFoundException, InterruptedException {
    long start = System.currentTimeMillis();
    Scanner in = new Scanner(new File(filename));
    n = in.nextInt();
    m = in.nextInt();
    int a[][] = new int[n][m];
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < m; ++j) {
        a[i][j] = in.nextInt();
      }
    }
    int b[][] = new int[n][m];
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < m; ++j) {
        b[i][j] = in.nextInt();
      }
    }
    int sum[][] = new int[n][m];
    ArrayList threads = new ArrayList();
    for (int i = 0; i < Math.min(n, T); ++i) {
      threads.add(matrixOperaterFactory.newInstance(i, T, a, b, sum, debug));
    }
    ExecutorService executorService = Executors.newFixedThreadPool(threadPoolSize);
    List<Future<Void>> futureList = executorService.invokeAll(threads);
    executorService.shutdownNow();
    double time = (System.currentTimeMillis() - start) / 1000.0;
    if (debug) {
      System.out.println("ThreadPoolSize: " + threadPoolSize);
      System.out.println("Number of threads: " + T);
      System.out.println("Operations took: " + time + " seconds");
    }
    return time;
  }

  public static void main(String[] args) throws IOException, InterruptedException {
    try (Writer fileWriter = new BufferedWriter(new OutputStreamWriter(
        new FileOutputStream("filename.txt"), "utf-8"))) {
      for (String add : adds) {
        for (int aTP : TP) {
          for (int aT : T) {
            double time = solve("data/" + add, aTP, aT, true, new AdditionerFactory());
            fileWriter.write("add ");
            fileWriter.write(String.valueOf(n));
            fileWriter.write(" ");
            fileWriter.write(String.valueOf(aTP));
            fileWriter.write(" ");
            fileWriter.write(String.valueOf(aT));
            fileWriter.write(" ");
            fileWriter.write(String.valueOf(time));
            fileWriter.write("\n");
          }
        }
      }
      for (String mult : mults) {
        for (int aTP : TP) {
          for (int aT : T) {
            double time = solve("data/" + mult, aTP, aT, true, new MultiplierFactory());
            fileWriter.write("mult ");
            fileWriter.write(String.valueOf(n));
            fileWriter.write(" ");
            fileWriter.write(String.valueOf(aTP));
            fileWriter.write(" ");
            fileWriter.write(String.valueOf(aT));
            fileWriter.write(" ");
            fileWriter.write(String.valueOf(time));
            fileWriter.write("\n");
          }
        }
      }
    }
  }
}

