A = [ 1 1 1 1;
      2 3 1 5;
      -1 1 -5 3;
      3 1 7 -2 ];

b = [ 10;
      31;
      -2;
      18 ];

function x = gauss(A, b)
  [_, n] = size(A);
  E = [A b];
  for p = 1:n-1
    [_, q] = max(abs(A(p:n, p)));
    q = q + p - 1;
    E([p q], :) = E([q, p], :);
    for j = p+1:n
      E(j, 1:n+1) = E(j, 1:n+1)-E(j, p) / E(p, p) * E(p, 1:n+1);
    end
  end
  x = zeros(1, n);
  A = E(1:n, 1:n);
  b = E(:, n+1);
  x(n) = b(n) / A(n, n);
  for i = n-1:-1:1
    x(i) = (b(i) - A(i, :) * x') / A(i, i);
  end
  x = x';
end

gauss(A, b)

A \ b
