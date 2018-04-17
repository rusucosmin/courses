f = @(x) x .* log(x);


function ret = rtf(a, b, n, f)
  x = linspace(a, b, n + 1);
  ret = (b - a) / (2 * n) * (f(a) + f(b) + 2 * sum(f(x(2:n))))
end

hold on;

a = 1;
b = 2;
h = (b - a) / 2;

ret = rtf(a, b, 10, f)
