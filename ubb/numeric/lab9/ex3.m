x = 1;

function ret = Hilber(n)
  ret = ones(n);
  for i = 1:n
    for j = 1:n
      ret(i, j) = 1 / (i + j - 1);
    end
  end
end

for n = 10:15
  cond(Hilber(n))
end
