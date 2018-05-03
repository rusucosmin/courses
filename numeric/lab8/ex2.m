f = @(x) 2 ./ (1 + x .^ 2)

function ret = romberg(f, a, b, precision)
  h = b - a;
  q_last = h / 2 * (f(a) + f(b));
  k = 0;
  while (1)
    k = k + 1;
    first_term =  q_last / 2;
    j = 1:(2^(k - 1));
    _sum = sum(f(a + (2 .* j - 1) / (2 ^ k) * h));
    second_term =  h / (2 ^ k) * _sum;
    q_k = first_term + second_term;
    if abs(q_k - q_last) <= precision
      break;
    end
    q_last = q_k;
  end
  ret = q_k;
end

function ret = simpson(f, a, b, precision)
  h = b - a;
  q_last = h / 2 * (f(a) + f(b));
  q_slast = h / 6 * (f(a) + 4 * f(a + h / 2) + f(b));
  q_slast = NaN;
  k = 0;
  while (1)
    k = k + 1;
    first_term = q_last / 2;
    j = 1:(2^(k - 1));
    _sum = sum(f(a + (2 .* j - 1) / (2 ^ k) * h));
    second_term =  h / (2 ^ k) * _sum;
    q_k = first_term + second_term;
    q_sk = (4 * q_k - q_last) / 3;
    if abs(q_sk - q_slast) <= precision
      break;
    end
    q_last = q_k;
    q_slast = q_sk;
  end
  ret = q_sk;
end

printf("%.10f\n", romberg(f, 0, 1, 0.00001))
printf("%.10f\n", simpson(f, 0, 1, 0.00001))
printf("%.10f\n", pi / 2)

