# Lab2 - MapReduce

## PySpark

Assignment:
1. Add up the sizes of all the lines in ”ex1.txt” using the map and reduce operations.

Solution
```python
lines = sc.textFile("lab2/ex1.txt")

#sum = lines.map(lambda x: ('sum', len(x))).reduceByKey(lambda x, y: x+y)
sum = lines.map(lambda x: len(x)).reduce(lambda x, y: x+y)

sum.take(1)
```

2. Use the reduceByKey() operation on key-value pairs to count how many times each line
of text occurs in a file.

Solution
```python
lines = sc.textFile("lab2/ex1.txt")

sum = lines.map(lambda x: (x, 1)).reduceByKey(lambda x, y: x + y)

sum.take(1)
```

3. Use sortByKey() to sort the key-value pairs alphabetically.
```python
lines = sc.textFile("lab2/ex1.txt")


sum = lines.map(lambda x: (x, 1)).reduceByKey(lambda x, y: x + y).sortByKey(ascending=True)

sum.take(1)
```
