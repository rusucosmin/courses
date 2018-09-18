NT=(localhost localhost,localhost localhost,localhost,localhost localhost,localhost,localhost,localhost)
NN=(100 200 500 1000 2000 5000 10000 20000)

echo "Building project..."
cmake .
make

> performance.log

for i in "${NT[@]}"; do
  for j in "${NN[@]}"; do
    start=$(gdate +%s.%N);
    echo $i $j >> performance.log
    echo "Testing with $i threads on a $jx$j matrix";
    mpirun --host $i ./GrayscaleFilter.o ~/dummy/path $j
    dur=$(echo "$(gdate +%s.%N) - $start" | bc);
    echo $dur >> performance.log
  done
done
