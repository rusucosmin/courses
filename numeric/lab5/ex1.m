Time = [0 3 5 8 13];
Distance = [0 225 383 623 993];
Speed = [75 77 80 74 72];

function ret = repelem(X, m)
  [_, n] = size(X);
  R = [[1:n]; m * ones(1, n)];
  ret = repelems(X, R);
end

function N = newton(x, f, X)
  A = div_diff_table(x, f);
  A = A(1,3:end);
  C = [ones(size(X')), cumprod(X' - x(1:end-1), dim=2)];
  N = A * C';
end

function ret = div_diff_table(a, f, df, X)
  aa = repelem(a, 2);
  n = 2 * length(a);
  table = aa';

  t_2 = repelem(f, 2);
  aux = diff(f) ./ diff(a);
  aux = [aux, NaN];
  t_3 = reshape([df; aux], 1, []);
  table = [t_2', t_3'];

  for i = 2:(n-1)
    a_diff = (table((i + 1):end, 2) .- table(1:(end-i), 2));
    last_col = (table(2:(end-i+1), end) - table(1:end-i, end));
    new_col = last_col ./ a_diff;

    table = [table, [new_col; NaN(i, 1)]];
  end

  table
  % compute the newtonw poly:
  dh = 0;
  for j = 1:n-1
    dh = dh + polyval(polyder(poly(aa(1:j))), X) * table(1, j+2);
  end

  ret = dh;
end

x = div_diff_table(Time, Distance, Speed, [10]);
printf("%2.f\n", x)
