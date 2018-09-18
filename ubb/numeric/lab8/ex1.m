f = @(x) e .^ (-x .^ 2)

function ret = areaRect(f, a, b)
  mid = (a + b) / 2;
  ret = (b - a) * f(mid);
end

function ret = areaRectMult(f, a, b, n)
  x1 = a + (b - a) / (2 * n);
  xn = x1 + (n - 1) * (b - a) / n;
  x = linspace(x1, xn, n);
  ret = (b - a) / n *  sum(f(x));
end

printf("%.10f\n", areaRect(f, 1, 1.5));
printf("%.10f\n", areaRectMult(f, 1, 1.5, 150));
printf("%.10f\n", areaRectMult(f, 1, 1.5, 500));
printf("%.10f\n", areaRectMult(f, 1, 1.5, 5000));
