x = [-5:0.1:5];
f = @(x) 1 + (1 ./ x .^ 2);

plot(x, f(x))

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

x = [-5:1:5];
X = [-5:0.5:5];

Y = lagrange(x, f(x), X)

hold on
plot(X, Y', 'x')

