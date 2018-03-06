T = @(n, t) cos(n * acos(t));
t = -1:0.01:1;

hold on;

title('Chebyshev polynomials')
plot(t, T(1, t), 'DisplayName', 'T1');
plot(t, T(2, t), 'DisplayName', 'T2');
plot(t, T(3, t), 'DisplayName', 'T3');
legend('T1', 'T2', 'T3');

leg = ['T1'; 'T2'; 'T3']

function ret = P(n)
  if (n == 0)
    ret = @(x) 1;
  elseif(n == 1)
    ret = @(x) x;
  else
    ret = @(x) 2 .* x .* P(n - 1)(x) - P(n - 2)(x);
  end
end

for i = 1:10
  plot(t, P(i)(t));
  leg = [leg; sprintf('T%d', i)];
end

legend(leg)
