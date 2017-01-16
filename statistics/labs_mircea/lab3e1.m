clear;
x0 = input('x0 = ');
x1 = input('x1 = ');
x2 = input('x2 (> x1) = ');
alfa = input('alfa (in (0; 1)) = ');
beta = input('beta (in (0; 1)) = ');

fprintf('1 for Normal\n');
fprintf('2 for T\n');
fprintf('3 for Chi Squared\n');
option = input('option = ');

switch option
    case 1
        % Normal Distribution
        mu = input('mu = ');
        sigma = input('sigma (> 0) = ');
        % a) P(X <= x0)
        pa = normcdf(x0, mu, sigma);
        % b) P(X >= x0)
        pb = 1.0 - pa;
        % c) P(x1 <= X <= x2)
        pc = normcdf(x2, mu, sigma) - normcdf(x1, mu, sigma);
        % d) P(X <= x1 or X >= x2)
        pd = 1.0 - pc;
        % e) x_alfa such that P(X < x_alfa) = alfa
        x_alfa = norminv(alfa, mu, sigma);
        % f) x_beta such that P(X > x_beta) = beta
        x_beta = norminv(1.0 - beta, mu, sigma);
    case 2
        n = input('n = ');
        % a) P(X <= x0)
        pa = tcdf(x0, n);
        % b) P(X >= x0)
        pb = 1.0 - pa;
        % c) P(x1 <= X <= x2)
        pc = tcdf(x2, n) - tcdf(x1, n);
        % d) P(X <= x1 or X >= x2)
        pd = 1.0 - pc;
        % e) x_alfa such that P(X < x_alfa) = alfa
        x_alfa = tinv(alfa, n);
        % f) x_beta such that P(X > x_beta) = beta
        x_beta = tinv(1.0 - beta, n);
    case 3
        n = input('n = ');
        % a) P(X <= x0)
        pa = chi2cdf(x0, n);
        % b) P(X >= x0)
        pb = 1.0 - pa;
        % c) P(x1 <= X <= x2)
        pc = chi2cdf(x2, n) - chi2cdf(x1, n);
        % d) P(X <= x1 or X >= x2)
        pd = 1.0 - pc;
        % e) x_alfa such that P(X < x_alfa) = alfa
        x_alfa = chi2inv(alfa, n);
        % f) x_beta such that P(X > x_beta) = beta
        x_beta = chi2inv(1.0 - beta, n);        
    otherwise
        fprintf('Invalid option.\n');
end

% Display.
if 1 <= option && option <= 3
    fprintf('Answer in part a) is %.4f\n', pa);
    fprintf('Answer in part b) is %.4f\n', pb);
    fprintf('Answer in part c) is %.4f\n', pc);
    fprintf('Answer in part d) is %.4f\n', pd);
    fprintf('Answer in part e) is %.4f\n', x_alfa);
    fprintf('Answer in part f) is %.4f\n', x_beta);
end