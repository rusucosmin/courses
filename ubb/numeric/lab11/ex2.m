A = [ 3 -1  0  0  0  0;
     -1  3 -1  0  0  0;
      0 -1  3 -1  0  0;
      0  0 -1  3 -1  0;
      0  0  0 -1  3 -1;
      0  0  0  0 -1  3 ];

b = [2; 1; 1; 1; 1; 2];

A1 = [ 3  1  1;
      -2  4  0;
      -1  2 -6 ];

b1 = [12; 2; -5]

function ret = solve(A, b, er)
  [n, n] = size(A);
  x = rand(n, 1);
  new_x = rand(n, 1);
  M = diag(diag(A));
  N = M - A;
  T = M \ N;
  c = M \ b;
  cnt = 0;
  while(norm(x - new_x) > er * (1 - norm(T)) / norm(T))
    x = new_x;
    new_x = T * x + c;
    cnt = cnt + 1;
  end
  cnt
  ret = x;
end

solve(A, b, 0.00001)
solve(A1, b1, 0.00001)

