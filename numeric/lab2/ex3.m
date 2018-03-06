x = -1:0.01:3;

function ret = P(n)
  if (n == 0)
    ret = @(x) 1;
  else
    ret = @(x) P(n - 1)(x) + x .^ n  / factorial(n);
  end
end

hold on;

leg = [];
for i = 0:6
  plot(x, P(i)(x));
  leg = [leg; sprintf('P%d', i)];
end

legend(leg);
title('First 6 Taylor polynomials');
