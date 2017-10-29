public interface MatrixOperaterFactory<T> {
  T newInstance(int i, int mod, int [][] a, int [][] b, int [][] sum, boolean debug);
}