import java.util.concurrent.Callable;

public class Multiplier extends Operater implements Callable<Void> {
  public Multiplier(int linesModuloClass, int mod, int [][] a, int [][] b, int[][] sum, boolean debug) {
    super(linesModuloClass, mod, a, b, sum, debug);
  }

  @Override
  public Void call() {
    if (debug) {
      System.out.println("Multiplier thread " + String.valueOf(linesModuloClass) + " started!");
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
      for (int k = 0; k < a[0].length; ++ k) {
        for (int j = 0; j < b.length; ++ j) {
          sum[i][j] += a[i][k] * b[k][j];
        }
      }
    }
    if (debug) {
      System.out.println("Multiplier thread " + String.valueOf(linesModuloClass) + " done!");
    }
    return null;
  }
}
