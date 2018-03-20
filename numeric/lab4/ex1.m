x = [1 2 3 4 5]
y = [22 23 25 30 28]

function ret = div_diff_table(a, f)
  [_, n] = size(a)
  table = a';
  table = [(0:(n-1))', table, f(a)'];

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
  A = A(1,3:end)
  C = cumprod(X - x)
  N = A * C'
end

newton(x, y, 2.5)
