x = 0:0.01:3;
y1 = x .^2 / 10;
plot(x, y1, 'r.:');
hold on;
y2 = x .* sin(x);
y3 = cos(x);
plot(x, y2);
plot(x, y3);
title('Cosmin Rusu');
legend('2nd polynomial', 'x * sin(x)', 'cos(x)', 'Location', 'NorthEast');


subplot(2, 2, 1);
plot(x, y1, 'r.:');
legend('2nd polynomial');

subplot(2, 2, 2);
plot(x, y2);
legend('x * sin(x)');

subplot(2, 2, 3);
plot(x, y3);
legend('cos(x)');
