a = input('a = ');
b = input('b(>a) = ');
n = input('n = ');

ind = 1:n; %length n
limits = a : (b - a) / n: b;  % length n + 1
leftlim = limits(1:n);
rightlim = limits(2:n + 1);

midp = (leftlim + rightlim) / 2;

results = [ind; leftlim; rightlim; midp];
fprintf('  Nr  |   Subint     | Midp |\n');
fprintf('%4d  | [%3.2f, %3.2f] | %3.2f | \n', results);
