import java.util.concurrent.Callable;

public class AdditionerFactory implements MatrixOperaterFactory<Callable<Void>> {
  @Override
  public Callable<Void> newInstance(int i, int mod, int[][] a, int[][] b, int[][] sum, boolean debug) {
    return new Additioner(i, mod, a, b, sum, debug);
  }
}
