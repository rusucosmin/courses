% Generate X e Geo(p)
clear ALL
p = input('probability of success = ');
X = 0;
while(rand >= p)
    X = X+1;
end;
clear X;

% Generate a sample
N = input('number of simulations = ');
for i = 1:N
    X(i) = 0;
    while(rand >= p)
        X(i) = X(i)+1;
    end;
end
UX = unique(X);
fr = hist(X, length(UX));
relfr = fr / N;

% Compare graphically to the Geo(n,p) distribution
n = input('number of trials = ');
xpdf = 1:n;
ypdf = geopdf(xpdf, p);
clf;
plot(xpdf, ypdf, 'bo', UX, relfr, 'rx');
legend('geopdf', 'simulation');