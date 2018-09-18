echo "Compiling classic"
g++ -O2 -std=c++11 -pthread -Dhome -Wall classic.cpp -o classic.o
echo "Compiling pollard_p"
g++ -O2 -std=c++11 -pthread -Dhome -Wall pollard_p.cpp -o pollard_p.o

echo "Generating test (this may take a while)"
python gen.py

for i in `ls tests`; do
  ./classic.o 'tests/'$i
  ./pollard_p.o 'tests/'$i
done

rm classic.o
rm pollard_p.o
