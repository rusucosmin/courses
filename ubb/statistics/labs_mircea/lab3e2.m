clear;

p = input('p in [0.05; 0.95] = ');

clf;

for n = 1:2:100
    xpdf = 0:n;
    ypdf = binopdf(xpdf, n, p);
    plot(xpdf, ypdf, 'r*:');
    pause(0.5);
end