l1 = @(x) x;
l2 = @(x) 3 / 2 .* x .^ 2 - 1 / 2;
l3 = @(x) 5 / 2 .* x .^ 3 - 3 / 2 .* x;
l4 = @(x) 35 / 8 .* x .^ 4 - 15 /4 .* x .^ 2 + 3 / 8;

x = 0:0.01:1;

subplot(2, 2, 1);
plot(x, l1(x))
title("l1(x)")
legend("l1(x)")
subplot(2, 2, 2);
plot(x, l2(x))
title("l2(x)")
legend("l2(x)")
subplot(2, 2, 3);
plot(x, l3(x))
title("l3(x)")
legend("l3(x)")
subplot(2, 2, 4);
plot(x, l4(x))
title("l4(x)")
legend("l4(x)")
