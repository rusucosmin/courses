x = [0:0.01:10];
f = @(x) 1 + cos(pi * x) ./ (1 + x);

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

x = [0:(10/20):10];
X = [0:0.01:10];

Y = lagrange(x, f(x), X);

hold on
plot(X, Y')

