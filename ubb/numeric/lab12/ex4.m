f = @(x) cos(x) - x

function ret = false_position(f, a, b, err)
  for n = 0:1000
    if abs(a - b) < err
      break
    end
    c = (a * f(b) - b * f(a)) / (f(b) - f(a));
    if f(a) * f(c) <= 0
      b = c;
    else
      a = c;
    end
  end
  ret = a
end

false_position(f, 0.5, pi / 4, 0.0001);
