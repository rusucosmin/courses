x = 1:2:115;
y = sqrt(x);

[_, m] = size(x);

f = [y'];

X = 115;

for i = 0:(m-1)
  for j = 0:i-1
    i = i + 1;
    j = j + 1;
    _det = det([f(j, j), x(j) - X; f(i, j), x(i) - X]);
    f(i, j+1) = 1 / (x(i) - x(j)) * _det;
    i = i - 1;
    j = j - 1;
  end
end

f(m, m)

