% Generate X e NB(p)
clear ALL
n = input('rank of success = ');
p = input('probability of success = ');
for j = 1:n
    Y(j) = 0;
    while(rand >= p)
        Y(j) = Y(j)+1;
    end;
end
X = sum(Y);
clear X;

% Generate a sample
N = input('number of simulations = ');
for i = 1:N
    for j = 1:n
        Y(j) = 0;
        while(rand >= p)
            Y(j) = Y(j)+1;
        end;
    end
    X(i) = sum(Y);
end
UX = unique(X);
fr = hist(X, length(UX));
relfr = fr / N;

% Compare graphically to the NB(n,p) distribution
xpdf = 1:100;
ypdf = nbinpdf(xpdf, n, p);
clf;
plot(xpdf, ypdf, 'bo', UX, relfr, 'rx');
legend('nbinpdf', 'simulation');