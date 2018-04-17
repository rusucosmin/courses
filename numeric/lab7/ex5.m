f = @(x) 1 ./ (4 + sin(20 .* x));

function ret = rtf(a, b, n, f)
  x = linspace(a, b, n + 1);
  ret = (b - a) / (6 * n) * (f(a) + f(b) + 2 * sum(f(x(2:n))) + 4 * sum(f((x(1:n) + x(2:n+1))/2)))
end

a = 0;
b = pi;

ret = rtf(a, b, 30, f)
