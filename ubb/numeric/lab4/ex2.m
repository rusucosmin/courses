x = [0:6/12:6];
f = @(x) exp(sin(x));
y = f(x);

function ret = div_diff_table(a, f)
  [_, n] = size(a);
  table = a';
  table = [(0:(n-1))', table, f'];

  for i = 1:(n-1)
    a_diff = (table((i + 1):end, 2) .- table(1:(end-i), 2));
    last_col = (table(2:(end-i+1), end) - table(1:end-i, end));
    new_col = last_col ./ a_diff;

    table = [table, [new_col; NaN(i, 1)]];
  end

  ret = table;
end

function N = newton(x, f, X)
  A = div_diff_table(x, f);
  A = A(1,3:end);
  C = [ones(size(X')), cumprod(X' - x(1:end-1), dim=2)];
  N = A * C';
end

X = 0:0.1:6;
Y = newton(x, y, X);

plot(x, y, "o")
hold on;
plot(X, Y, "x")
