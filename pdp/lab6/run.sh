echo "Compiling naive algorithm - seq_1.cpp'"
g++ -O2 -std=c++11 -pthread -Dhome -Wall seq_1.cpp -o seq_1.o
echo "Compiling naive algorithm (threaded) - seq_1.cpp'"
g++ -O2 -std=c++11 -pthread -Dhome -Wall seq_2.cpp -o seq_2.o
echo "Compiling karasuba algorithm - kar_1.cpp'"
g++ -O2 -std=c++11 -pthread -Dhome -Wall kar_1.cpp -o kar_1.o
echo "Compiling karasuba algorithm (threaded) - kar_1.cpp'"
g++ -O2 -std=c++11 -pthread -Dhome -Wall kar_2.cpp -o kar_2.o

echo ""

for i in `ls tests/*.in`
do
  echo "Running test $i"
  head -n1 $i
  ./seq_1.o $i
  ./seq_2.o $i
  ./kar_1.o $i
  ./kar_2.o $i
  echo ""
done

rm *.o
