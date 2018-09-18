clear;
alpha = input('significance level (0; 1) = ');
X1 = [22.4 21.7 24.5 23.4 21.6 23.3 22.4 21.6 24.8 20.0];
X2 = [17.7 14.8 19.6 19.6 12.1 14.8 15.4 12.6 14.0 12.2];

% a)
% H0 :  sigma1 = sigma2 <=> (sigma1^2)/(sigma2^2) = 1
% H1 : sigma1 != sigma2 <=> (sigma1^2)/(sigma2^2) != 1
[h, p, ci, stats] = vartest2(X1, X2, 'alpha', alpha, 'tail', 'both');

if h == 0
    fprintf('H0 is NOT rejected, i.e. the population variances are equal\n');
    vartype = 'equal';
else
    fprintf('H0 is rejected, i.e. the population variances are NOT equal\n');
    vartype = 'unequal';
end

fprintf('P-value is %3.4f\n', p);
fprintf('Observed value of the test statistics is %3.4f\n', stats.fstat);
q1 = finv(alpha/2, stats.df1, stats.df2);
q2 = finv(1-alpha/2, stats.df1, stats.df2);
fprintf('Rejection region is (-inf, %3.4f) U (%3.4f, +inf)\n', q1, q2);

% b)
% H0 : miu1 = miu2 <=> miu1 - miu2 = 0
% H1 : miu1 > miu2 <=> miu1 - miu2 > 0
[h, p, ci, stats] = ttest2(X1, X2, 'alpha', alpha, 'tail', 'right', 'vartype', vartype);

if h == 0
    fprintf('H0 is NOT rejected, i.e. the gas mileage does NOT seem to be higher for premium\n');
else
    fprintf('H0 is rejected, i.e. the gas mileage seems to be higher for premium\n');
end

fprintf('P-value is %e\n', p);
fprintf('Observed value of the test statistics is %3.4f\n', stats.tstat);
qa = tinv(1-alpha, stats.df);
fprintf('Rejection region is (%3.4f, +inf)\n', qa);
