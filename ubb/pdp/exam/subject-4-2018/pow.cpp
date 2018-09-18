void pow(Mat a, int n) {
  Mat ret = Mat.eye(n);
  for(; n ; n /= 2) {
    if(n & 1)
      ret = Mat.mult(ret, a, T);
    a = Mat.mult(a, a, T);
  }
  return ret;
}
