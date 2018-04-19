# Lab 3

## Assignments
- [x] Import only the column order_status from the table orders, as text files (default).

```
$ sqoop import \
--connect "jdbc:mysql://quickstart.cloudera:3306/retail_db" \
--username=retail_dba \
--password=cloudera \
--table orders \
--columns order_status
--target-dir /orders
```
- [x] Using pyspark with (one of) the resulted data files, print how many times each order_status appears in that file.

```python
$ pyspark

lines = sc.textFile("/lab3/orders")

sum = lines.map(lambda x: (x.split(',')[-1], 1)).reduceByKey(lambda x, y: x + y)c

sum.take(10)
```

`movie (digital_visa, title, year, type, nb_spec, budget)`
`has_played_in (first_name_actor, last_name_actor, digital_visa) -`

### Create the tables
```
CREATE TABLE movie(
  digital_visa varchar(50),
  title varchar(50),
  year int,
  type varchar(50),
  nb_spec int,
  budget float
);

CREATE TABLE has_played_in(
  first_name_actor varchar(50),
  last_name_actor varchar(50),
  digital_visa varchar(50)
);

```

### Populate the database
```
 INSERT INTO movie values ('1234-5678-9012-3456', 'The Lego Movie', 2017, 'cartoon', 10, 100000.5);
```

### Import movies
```
sqoop import --connect "jdbc:mysql://localhost/userdb" --username root --password cloudera --table movie --m 5 --target-dir /lab3 --split-by digital_visa
```

```
hadoop fs -cat /lab3/part-m-*
```

### Import has_played_in

```
hadoop fs -cat /lab3/has_played_in/part-m-*
```


###
- [x] Execute all the above commands listed in exercise 1 and 2.
- [x] In your database, create the two tables in exercise 2 and populate them. You may use any kind of database, but have to provide an appropriate URL for the server in order to connect to the DB.
- [x] Import the movies released in the 90s.
```
$ sqoop import --connect "jdbc:mysql://localhost/userdb" --username root --password cloudera --table movie --m 5 --target-dir /lab3/movies-1990 --split-by digital_visa --where "year = 1990";

$ hadoop fs -cat /lab3/movies-1990/*
```
- [x] Import the movies having a production budget less than 1.5 million dollars and a number of spectators greater than 10 million.
```
$ sqoop import --connect "jdbc:mysql://localhost/userdb" --username root --password cloudera --table movie --m 5 --target-dir /lab3/movies-popular --split-by digital_visa --where "nb_spec >= 10000000 AND budget < 1500000";

$ hadoop fs -cat /lab3/movies-popular/*
```
- [x] Import the animation movies released in 2012 and in 2013.
```
$ sqoop import --connect "jdbc:mysql://localhost/userdb" --username root --password cloudera --table movie --m 5 --target-dir /lab3/movies-animation --split-by digital_visa --where "type = 'animation' AND (year in (2012, 2013))";

$ hadoop fs -cat /lab3/movies-animation/*
```
- [x] Import the table has_played_in into HDFS.
```
$ sqoop import --connect "jdbc:mysql://localhost/userdb" --username root --password cloudera --table has_played_in --m 5 --target-dir /lab3/has_played_in --split-by digital_visa
```
- [x] Using pyspark with the files resulted from the previous import (table has_played_in), count how many times Johnny Depp has played in a movie.

```
lines = sc.textFile("/lab3/has_played_in")

sum = lines.map(lambda x: (" ".join(x.split(',')[0:-1]), 1)).reduceByKey(lambda x, y: x + y)

sum.take(9)
```
