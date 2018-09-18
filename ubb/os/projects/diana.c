///...R2...
///Write a program which creates 2 child processes. The parent sends to 
///its children its own pid through fifos. Each child sends to the other 
///one its own pid and 0 if the difference between its own pid and parent 
///pid is less than 2 and 1 otherwise.
