clear;
alpha = input('significance level (0; 1) = ');
% H0 : miu = 99.4
% H1 : miu > 99.4 (right-tailed test)
X = [99.8 * ones(1,2), ...
     99.9 * ones(1,5), ...
     98.0 * ones(1,3), ...
     100.1 * ones(1,4), ...
     100.5 * ones(1,2), ...
     100.0 * ones(1,2), ...
     100.2 * ones(1,2)];
miu0 = 99.4;
 
[h, p, ci, stats] = ttest(X, miu0, alpha, 'right');
tstat = stats.tstat;

if h == 0
    fprintf('H0 is NOT rejected, i.e. the center will accept the energy bars\n');
else
    fprintf('H0 is rejected, i.e. the center will NOT accept the energy bars\n');
end

fprintf('P-value is %3.4f\n', p);
fprintf('Observed value of the test statistics is %3.4f\n', tstat);

df = stats.df;
qa = tinv(1-alpha, df);
fprintf('Rejection region is (%3.4f; +inf)\n', qa);
