f = @(x) (x - 2) ^ 2 - log(x);

function ret = bisect(f, a, b, err)
  for n = 0:1000
    if abs(a - b) < err
      break
    end
    c = (a + b) ./ 2;
    if f(a) * f(c) <= 0
      b = c;
    else
      a = c;
    end
  end
  ret = a
end

bisect(f, 1, 2, 0.0001);
