# Polynomials

# 1. Evaluate the polynomial p(x) = 2*x^3 - 5^x + 8
# in x = 2: (Use: polyval)

#x = 0:50;
#y = [];
#for i=1:51
#  if mod(x(i), 2) == 0
#    y = [y x(i) / 2];
#  else
#    y = [y 3 * x(i) + 1];
#  end
#end

#x = 0:50;
#y = x / 2;
#y(2:2:end) = 3 * x(2:2:end) + 1;

#plot(x, y, '*')

pb1(100);
pb1_rec(100);
