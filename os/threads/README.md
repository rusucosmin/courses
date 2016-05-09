#Threads
1. Implement a program that writes a number between 0 and 9 in a global variable and then creates 10 threads.
Each thread will check the global variable and if its value is the order number of the thread (given from
main at creation time), the thread writes in the global variable another number between 0 and 9 (different
than its own). The program ends when the global variable is changed 20 times.
    - FILE: cosmin.c

2. Calculate the sum of the elements in a bidimensional matrix, using a separate thread to calculate the sum
of each row. The main thread adds up these sums printing the final result.
    - FILE: robert.c

3. Implement a program that creates two threads. The threads will print their ID (pthread_self) 10 times and then
stop. Insure that the printed IDs alternate always (ie A, B, A, B, ...)
    - FILE: serg.c

4. Implement a program that gets as arguments a file name followed by words. For each word, create a separate
thread that counts its appearances in the given file.  Print out the sum of the appearances of all words.
    - FILE: andra.c - personal implementation
    - FILE: stana.c - Andra Stana's implementation (ugly, right?)

