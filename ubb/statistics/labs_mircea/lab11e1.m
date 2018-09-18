clear;
alpha = input('significance level (0; 1) = ');

% a)
% H0 : miu = 9
% H1 : miu < 9 (left-tailed test)
X = [7 7 4 5 9 9 ...
	 4 12 8 1 8 7 ...
     3 13 2 1 17 7 ...
     12 5 6 2 1 13 ...
     14 10 2 4 9 11 ...
     3 5 12 6 10 7];
sigma = 5; % sigma known
miu0 = 9; % test value

[h, p, ci, zval] = ztest(X, miu0, sigma, alpha, 'left');

if h == 0
    fprintf('H0 is NOT rejected, i.e. the standard is met\n');
else
    fprintf('H0 is rejected, i.e. the standard is NOT met\n');
end

fprintf('P-value is %3.4f\n', p);
fprintf('Observed value of the test statistics is %3.4f\n', zval);

qa = norminv(alpha, 0, 1);
fprintf('Rejection region is (-inf, %3.4f)\n', qa);

% ---------------
% b)
% H0 :  sigma = 5 <=> sigma^2 = 25
% H1 : sigma != 5 <=> sigma^2 != 25 (two-tailed test)
var0 = sigma^2;
[h, p, ci, stats] = vartest(X, var0, alpha, 'both');

if h == 0
    fprintf('H0 is NOT rejected, i.e. the assumption on sigma seems to be correct\n');
else
    fprintf('H0 is rejected, i.e. the assumption on sigma does NOT seem to be correct\n');
end

fprintf('P-value is %3.4f\n', p);
fprintf('Observed value of the test statistics is %3.4f\n', stats.chisqstat);
q1 = chi2inv(alpha/2, stats.df);
q2 = chi2inv(1-alpha/2, stats.df);
fprintf('Rejection region is (-inf, %3.4f) U (%3.4f, +inf)\n', q1, q2);
