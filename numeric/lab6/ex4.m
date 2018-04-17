axis([0, 3, 0, 5])
[x, y] = ginput(10);

P2 = polyfit(x, y, 2);

hold on;
plot(x, y, 'x');
x_ext = 0:0.1:3
plot(x_ext, polyval(P2, x_ext));
