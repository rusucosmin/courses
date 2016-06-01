g++ -std=c++11 -Wall -Wextra -lm -O2 sol.cpp

for i in `seq 20`;
do
    echo "Generation "test$((i-1)).ok""
    cat "test$((i-1)).in" | ./a.out > "test$((i-1)).ok"
done

rm a.out
