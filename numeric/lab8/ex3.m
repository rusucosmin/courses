f = @(x) 100 ./ (x .^ 2) .* sin(10 ./ x);

function ret = Simpson(f, a, b)
  ret = (b - a) / 6 * (f(a) + 4 * f((a + b) / 2) + f(b));
end

function I = adquad(f, a, b, er)
  I1 = Simpson(f, a, b);
  I2 = Simpson(f, a, (a+b)/2) + Simpson(f, (a+b)/2, b);
  if abs(I1 - I2) < 15 * er
    I = I2;
  else
    I = adquad(f, a, (a+b)/2, er/2) + adquad(f, (a+b)/2, b, er/2);
  end
end

fplot(f, [1, 3])
printf("%.10f\n", adquad(f, 1, 3, 0.0001));
