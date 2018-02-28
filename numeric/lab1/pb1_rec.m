function retval = pb1_rec(n)
  if (n == 1)
    retval = 1.5;
  else
    retval = 1 + 1 / (1 + pb1_rec(n - 1));
  endif
endfunction
