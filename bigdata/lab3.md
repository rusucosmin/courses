# Lab 3

* ```Import only the column order_status from the table orders, as text files (default)..```

```
$ sqoop import \
--connect "jdbc:mysql://quickstart.cloudera:3306/retail_db" \
--username=retail_dba \
--password=cloudera \
--table orders \
--columns order_status
--target-dir /orders
```

```python
$ pyspark

lines = sc.textFile("lab2/ex1.txt")

sum = lines.map(lambda x: (x, 1)).reduceByKey(lambda x, y: x + y)

sum.take(9)
```
