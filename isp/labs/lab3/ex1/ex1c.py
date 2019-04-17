import csv
from datetime import datetime

com402_db = []
MyMovies = []

with open('com402-3.csv', mode='r') as infile:
    reader = csv.reader(infile)
    for row in reader:
        com402_db.append((row[0], row[1][1:], row[2][1:], row[3]))

with open('imdb-3.csv', mode='r') as infile:
    reader = csv.reader(infile)
    for row in reader:
        key = row[0]
        if (key == "cosmin.rusu@epfl.ch"):
            MyMovies.append((row[1][2:-1], row[2][1:], row[3]))

List = []
for i in range(0,50):
    List.append([])

j = 0
for Movie_Date in MyMovies:
    x = Movie_Date[1]
    date = datetime(day=int(x[0:2]), month=int(x[3:5]), year=int("20" + x[6:8]))
    for HashRow in com402_db:
        y = HashRow[2]
        date2 = datetime(day=int(y[0:2]), month=int(y[3:5]), year=int("20" + y[6:8]))
        diff = abs((date2 - date).days)
        if (diff >=0 and diff <= 13):
            List[j].append(HashRow[0])
    List[j] = list(set(List[j]))
    j = j + 1

MyHash = ''
S = set(List[0])
for k in range(0,49):
    S = S.intersection(List[k+1])
print("This is my Hash " + list(S)[0])
MyHash = list(S)[0]

MyHashedMovies = []
for HashRow in com402_db:
    if (HashRow[0] == MyHash):
        MyHashedMovies.append((HashRow[1], HashRow[2], HashRow[3]))

print(MyHashedMovies[5][0])

TempList = []
for Movie in MyMovies:
    count = 0
    x = Movie[1]
    date = datetime(day=int(x[0:2]), month=int(x[3:5]), year=int("20" + x[6:8]))
    for HashMovie in MyHashedMovies:
        y = HashMovie[1]
        date2 = datetime(day=int(y[0:2]), month=int(y[3:5]), year=int("20" + y[6:8]))
        diff = abs((date2 - date).days)
        if (diff >=0 and diff <= 13 and HashMovie[2] == Movie[2]):
            count = count + 1
    if (count == 1):
        TempList.append((Movie[0], HashMovie[0]))

for my_mov_hash in MyHashedMovies:
  for temp in TempList:
    if temp[1] == my_mov_hash[0]:
      print(temp[0])
