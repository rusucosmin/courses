import java.util.concurrent.Callable;

public class Additioner extends Operater implements Callable<Void> {
  public Additioner(int linesModuloClass, int mod, int [][] a, int [][] b, int[][] sum, boolean debug) {
    super(linesModuloClass, mod, a, b, sum, debug);
  }

  @Override
  public Void call() {
    if (debug) {
      System.out.println("Additioner thread " + String.valueOf(linesModuloClass) + " started!");
    }
    if (a.length == 0) {
      return null;
    }
    if (a[0].length == 0) {
      return null;
    }
    if (mod == 0) {
      return null;
    }
    for (int i = linesModuloClass; i < a.length; i += mod) {
      for (int j = 0; j < a[i].length; ++ j) {
        sum[i][j] = a[i][j] + b[i][j];
      }
    }
    if (debug) {
      System.out.println("Additioner thread " + String.valueOf(linesModuloClass) + " ended!");
    }
    return null;
  }
}
