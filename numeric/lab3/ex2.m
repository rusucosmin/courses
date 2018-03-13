x = [81 100 144];
f = [9 10 12];
X = [115]

function A = a(x)
  [_, n] = size(x);
  ret = [];
  for i = 1:n
    diff = x(i) - x;
    prd = prod(diff(1:i-1)) * prod(diff(i+1:end));
    ret = [ret, 1 / prd];
  end
  A = ret;
end

function L = lagrange(x, f, X)
  A = a(x);
  num = sum(A .* f ./ (X' - x), ind=2);
  denom = sum(A ./ (X' - x), ind=2);
  L = num ./ denom;
end

plot(x, f, 'x')

Y = lagrange(x, f, X)

hold on

plot(X, Y', 'o')
