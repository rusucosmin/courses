h = 0.25;
a = 1;
a = @(i) a + i * h;
f = @(x) sqrt(5 .* x .^ 2 + 1);

function ret = diff_table(a, f)
  [_, n] = size(a)
  table = a';
  table = [(0:(n-1))', table, f(a)'];

  for i = 1:(n-1)
    last_col = table(2:end, end) - table(1:end-1, end);

    table = [table, [last_col; nan]];
  end

  ret = table;
end

diff_table(a(0:5), f)
