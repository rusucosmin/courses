echo "Compiling solution"
g++ -O2 -std=c++11 -pthread -Dhome -Wall cycle.cpp -o cycle.o
dir="tests/"

for i in `seq 10`; do
  python cycle_gen.py -s small -i $dir$i.in
  cp $dir$i.in "cycle.in"
  ./cycle.o
done

for i in `seq 11 20`; do
  python cycle_gen.py -s medium -i $dir$i.in
  cp $dir$i.in "cycle.in"
  ./cycle.o
done

for i in `seq 21 30`; do
  python cycle_gen.py -s large -i $dir$i.in
  cp $dir$i.in "cycle.in"
  ./cycle.o
done

for i in `seq 31 34`; do
  python cycle_gen.py -s small -i $dir$i.in -o no-cycle
  cp $dir$i.in "cycle.in"
  ./cycle.o
done

for i in `seq 35 37`; do
  python cycle_gen.py -s medium -i $dir$i.in -o no-cycle
  cp $dir$i.in "cycle.in"
  ./cycle.o
done

for i in `seq 38 40`; do
  python cycle_gen.py -s large -i $dir$i.in -o no-cycle
  cp $dir$i.in "cycle.in"
  ./cycle.o
done

echo "All tests passes"

rm cycle.o
