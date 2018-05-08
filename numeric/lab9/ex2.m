A = [ 10 7 8 7;
      7 5 6 5;
      8 6 10 9;
      7 5 9 10 ];

b = [ 32;
      23
      33
      31 ];

x = A \ b
cond(A)

bb = [ 32.1;
       22.9;
       33.1;
       30.9 ];

xb = A \ bb

rel_err_x = norm(b - bb) / norm(b)

rel_err_y = norm(x - xb) / norm(xb)

rel_err_x / rel_err_y

Ab = [ 10 7 8.1 7.2;
       7.08 5.04 6 5;
       8 5.98 9.89 9;
       6.99 4.99 9 9.98 ];

xb = Ab \ b;

rel_err_A = norm(A - Ab) / norm(A)

norm(x - xb) / norm(x) / rel_err_A



