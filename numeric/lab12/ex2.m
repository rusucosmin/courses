f = @(x) x ^ 3 - x ^ 2 - 1

function ret = secant(f, x0, x1, maxIter, err)
  for n = 1:maxIter
    if abs(x1 - x0) < err
      break
    end
    x = x1 - (x1 - x0) / (f(x1) - f(x0)) * f(x1);
    x0 = x1;
    x1 = x;
  end
  ret = x1
end

x = secant(f, 1, 2, 100, 0.0001);
