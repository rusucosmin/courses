public class Operater {
  protected int linesModuloClass, mod;
  protected int [][] a, b, sum;
  protected boolean debug;

  public Operater(int i, int mod, int [][] a, int [][] b, int [][] sum, boolean debug) {
    this.linesModuloClass = i;
    this.mod = mod;
    this.a = a;
    this.b = b;
    this.sum = sum;
    this.debug = debug;
  }
}
