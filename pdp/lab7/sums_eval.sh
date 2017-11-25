echo "Compiling solution"
g++ -O2 -std=c++11 -pthread -Dhome -Wall sums.cpp -o sums.o
dir="tests/sums/"

for i in `seq 10`; do
  python sums_gen.py -s small -i $dir$i.in -o $dir$i.ok
  cp $dir$i.in "sums.in"
  ./sums.o
  lines=`diff "sums.out" $dir$i.ok | wc | awk '{print $1}'`
  if [ $lines -gt 0 ]; then
    echo "Test failed"
    diff "sums.out" $dir$i.ok
    exit 2
  fi
done

for i in `seq 11 20`; do
  python sums_gen.py -s medium -i $dir$i.in -o $dir$i.ok
  cp $dir$i.in "sums.in"
  ./sums.o
  lines=`diff "sums.out" $dir$i.ok | wc | awk '{print $1}'`
  if [ $lines -gt 0 ]; then
    echo "Test failed"
    diff "sums.out" $dir$i.ok
    exit 2
  fi
done

for i in `seq 21 30`; do
  python sums_gen.py -s large -i $dir$i.in -o $dir$i.ok
  cp $dir$i.in "sums.in"
  ./sums.o
  lines=`diff "sums.out" $dir$i.ok | wc | awk '{print $1}'`
  if [ $lines -gt 0 ]; then
    echo "Test failed"
    diff "sums.out" $dir$i.ok
    exit 2
  fi
done

echo "All tests passes"

rm sums.o
