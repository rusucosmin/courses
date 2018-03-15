# Intro to Big Data - Lab 1

- [x] Installed the Cloudera VM with Hadoop
- [x] [Lab 1 pdf](https://drive.google.com/file/d/1g3vCwrrBJF1jUgramF3bG1-nEbPqTzes/view)

## Assignment

1. Read the input from stdin and write to the HDFS home directory in “file1.txt” (using
put).

Solution
```bash
$ cat | hadoop fs -put - file1.txt
```

2. Create a new directory “src” and populate it with two text files “file1.txt” and
“file2.txt”. Concatenate “file1” and “file2” into the text file “output.txt” (outside of
the directory “src”) using getmerge.
What do you observe, where is “output.txt” created? Display the contents of
“output.txt”.

Solution
```bash
# create the directory and the two files inside
$ hadoop fs -mkdir src
$ echo "file1.txt" | hadoop fs -put - src/file1.txt
$ echo "file2.txt" | hadoop fs -put - src/file2.txt
$ hadoop fs -getmerge -nl src/file1.txt src/file2.txt output.txt
# the file is saved locally
$ cat output.txt
```

3. Copy the file “output.txt” between the local file system and hdfs using get.

Solution
```bash
$ hadoop fs -get src/file1.txt
```

4. Display the number of directories, files and bytes under “lab1” using count.

Solution
```bash
$ hadoop fs -count src
```

5. Print all files under the “src” directory using find.

Solution
```bash
$ hadoop fs -find src
```

6. In a file “textFile.txt” print all .txt files that begin with “file” using find.

Solution
```bash
$ hadoop fs -find src -name '*.txt' > textFile.txt
```
