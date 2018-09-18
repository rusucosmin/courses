NT=(1 3 5 10 15 25 50 100 250 500)
NN=(100 1000 2000 5000 10000 20000)

echo "Building project..."
cmake .
make

> performance.log

for i in "${NT[@]}"; do
  for j in "${NN[@]}"; do
    start=$(gdate +%s.%N);
    echo $i $j >> performance.log
    echo "Testing with $i threads on a $jx$j matrix";
    ./GrayscaleFilter.o ~/dummy/path $i $j;
    dur=$(echo "$(gdate +%s.%N) - $start" | bc);
    echo $dur >> performance.log
  done
done
