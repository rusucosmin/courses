from datetime import datetime, timedelta

dedis_db = []
MyMovies = []
MovieList = []


with open('com402-3.csv', mode='r') as infile:
    for line in infile.readlines():
        row = line.split(', ')
        if (len(row) != 4):
          print(row)
          assert False
        dedis_db.append((row[0], row[1][1:], row[2], row[3]))

AllUsers = []
with open('imdb-3.csv', mode='r') as infile:
    for line in infile.readlines():
        row = line.split(", ")
        if (len(row) != 4):
          row = [row[0], ", ".join(row[1:-2]), row[-2], row[-1]]
        AllUsers.append(row[0])
AllUsers = list(set(AllUsers))


CosminHash = "6cebf0e64d997afc03d8fe31bb1a783120a2a8271be6d040259786dc0aef70c9"
CosminHashedMovies = []
for HashRow in dedis_db:
    if (HashRow[0] == CosminHash):
        CosminHashedMovies.append(HashRow[1])
print(len(CosminHashedMovies))

CosminC = 0

#Get the Hash-Movie Pair for every movie
for user in AllUsers:

    if (len(CosminHashedMovies) == 0):
        break 

    MyMovies = []
    with open('imdb-3.csv', mode='r') as infile:
        for line in infile.readlines():
            row = line.split(", ")
            if (len(row) != 4):
              row = [row[0], ", ".join(row[1:-2]), row[-2], row[-1]]
            key = row[0]
            if (key == user):
                MyMovies.append((row[1][1:], row[2], row[3]))
    List = []
    for i in range(0,50):
        List.append([])

    j = 0
    for Movie_Date in MyMovies:
        x = Movie_Date[1]
        day, month, year = x.split('/')
        date = datetime(day=int(day), month=int(month), year=int("20" + year))
        for HashRow in dedis_db:
            y = HashRow[2]
            day, month, year = y.split('/')
            date2 = datetime(day=int(day), month=int(month), year=int("20" + year))
            diff = abs((date2 - date).days)
            if (diff >=0 and diff <= 13):
                List[j].append(HashRow[0])
        List[j] = list(set(List[j]))
        j = j + 1

    S = set(List[0])
    for k in range(0,49):
        S = S.intersection(List[k+1])

    if (len(list(S)) == 1):
        MyHash = list(S)[0]
        MyHashedMovies = []
        for HashRow in dedis_db:
            if (HashRow[0] == MyHash):
                MyHashedMovies.append((HashRow[1], HashRow[2], HashRow[3]))

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
                    Z = HashMovie

            if (count == 1):

                if (len(CosminHashedMovies) == 0):
                    break 

                for CosminMovieCount in range(0, len(CosminHashedMovies)):
                    if (Z[0] == CosminHashedMovies[CosminMovieCount]):
                        print(Movie[0][:-1])
                        CosminHashedMovies.remove(Z[0])
                        CosminC = CosminC + 1
                        break

print(CosminC)

