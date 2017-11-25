echo "Compiling solution"
g++ -O2 -std=c++11 -pthread -Dhome -Wall add.cpp -o add.o
dir="tests/add/"

for i in `seq 10`; do
  python add_gen.py -s small -i $dir$i.in -o $dir$i.ok
  cp $dir$i.in "add.in"
  ./add.o
  lines=`diff "add.out" $dir$i.ok | wc | awk '{print $1}'`
  if [ $lines -gt 0 ]; then
    echo "Test failed"
    diff "add.out" $dir$i.ok
    exit 2
  fi
done

for i in `seq 11 20`; do
  python add_gen.py -s medium -i $dir$i.in -o $dir$i.ok
  cp $dir$i.in "add.in"
  ./add.o
  lines=`diff "add.out" $dir$i.ok | wc | awk '{print $1}'`
  if [ $lines -gt 0 ]; then
    echo "Test failed"
    diff "add.out" $dir$i.ok
    exit 2
  fi
done

for i in `seq 21 30`; do
  python add_gen.py -s large -i $dir$i.in -o $dir$i.ok
  cp $dir$i.in "add.in"
  ./add.o
  lines=`diff "add.out" $dir$i.ok | wc | awk '{print $1}'`
  if [ $lines -gt 0 ]; then
    echo "Test failed"
    diff "add.out" $dir$i.ok
    exit 2
  fi
done

echo "All tests passes"

rm add.o
