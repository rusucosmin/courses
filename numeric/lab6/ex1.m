Time = [1, 2, 3, 4, 5, 6, 7];
Temperature = [13, 15, 20, 14, 15, 13, 10];

function [a, b] = lsum(x, y)
  [_, m] = size(x);
  a = m * x * y' - sum(x) * sum(y);
  a = a / (m * (x * x') - sum(x) ^ 2);

  b = (x * x') * sum(y) - (x * y') * sum(x);
  b = b / (m * (x * x') - sum(x) ^ 2);
end

[a, b] = lsum(Time, Temperature)

plot(Time, Temperature, 'x');
hold on;
x = 1:0.01:10;
[_, n] = size(Time);
plot(x, a * x + b);
for i = 1:n
  plot([Time(i), Time(i)], [Temperature(i), Time(i) * a + b]);
end

E = norm(Temperature - a * Time - b) ^ 2
