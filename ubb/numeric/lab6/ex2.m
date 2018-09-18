x = -3:0.4:3;
y = sin(x);

P1 = polyfit(x, y, 1);
P2 = polyfit(x, y, 2)

hold on;
plot(x, y, 'x');
hold on;
_x = -3:0.1:3;
plot(_x, polyval(P1, _x));
hold on;
plot(_x, polyval(P2, _x));

