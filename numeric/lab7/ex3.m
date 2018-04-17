r = 110;
p = 75;
H = @(x) 60 * r / (r ^ 2 - p ^ 2) * ((1 - (p / r) ^ 2 .* sin(x))) .^ 0.5


function ret = rtf(a, b, n, f)
  x = linspace(a, b, n + 1);
  ret = (b - a) / (2 * n) * (f(a) + f(b) + 2 * sum(f(x(2:n))))
end

hold on;

a = 0;
b = 2 * pi;
h = (b - a) / 2;

ret = rtf(a, b, 10, H)
