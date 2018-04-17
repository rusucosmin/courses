f = @(x) 2 ./ sqrt(pi) * e .^ (-1 * x .^ 2);

function ret = rtf(a, b, n, f)
  x = linspace(a, b, n + 1);
  ret = (b - a) / (6 * n) * (f(a) + f(b) + 2 * sum(f(x(2:n))) + 4 * sum(f((x(1:n) + x(2:n+1))/2)));
end

a = 0;
b = 0.5;

ret = rtf(a, b, 4, f)
ret = rtf(a, b, 10, f)
