f = @(x) cos(x) - x
fd = @(x) -sin(x) - 1

function ret = newton(f, fd, x0, maxIter, err)
  for n = 1:maxIter
    x1 = x0 - f(x0) / fd(x0);
    if abs(x1 - x0) < err
      break
    end
    x0 = x1;
  end
  ret = x0
end

x = newton(f, fd,  pi/4, 100, 0.0001);
