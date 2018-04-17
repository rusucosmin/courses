f = @(x) 2 ./ (1 + x .^ 2);

hold on;

a = 0;
b = 1;
h = (b - a) / 2;

x = [a, a + h, b];

x = a:0.01:b;
y = f(x);

plot(x, y);
hold on;
plot([0, 1], [f(0), f(1)]);
ylim([0, 2]);

area = (b - a) / 6 * (f(a) + 4 * f((a + b) / 2) + f(b))
