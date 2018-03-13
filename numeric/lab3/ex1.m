x = [1930 1940 1950 1960 1970 1980];
f = [123203 131669 150697 179323 203212 226505];
X = [1955 1995];

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
