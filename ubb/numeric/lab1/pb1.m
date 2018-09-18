function retval = pb1(n)
  y = 1;
  for i=1:n
    y = 1 + 1 / (1 + y);
  end
  retval = y
end
