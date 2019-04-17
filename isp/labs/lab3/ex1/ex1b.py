import csv
import operator

com_dict = {}
with open('com402-2.csv', mode='r') as infile:
  reader = csv.reader(infile)
  for row in reader:
    key = row[1][2:-1]
    if not key in com_dict:
      com_dict[key] = 0
    com_dict[key] += 1

imdb_dict = {}
with open('imdb-2.csv', mode='r') as infile:
  reader = csv.reader(infile)
  for row in reader:
    key = row[1][2:-1]
    if not key in imdb_dict:
      imdb_dict[key] = 0
    imdb_dict[key] += 1

com_dict_sorted = sorted(com_dict.items(), key=lambda x: (x[1], x[0]))
imdb_dict_sorted = sorted(imdb_dict.items(), key=lambda x: (x[1], x[0]))

print(com_dict_sorted)
print(imdb_dict_sorted)

user_movies = {}
with open('com402-2.csv', mode='r') as infile:
  reader = csv.reader(infile)
  for row in reader:
    email = row[0].strip()
    if email not in user_movies:
      user_movies[email] = []
    if row[1][2:-1] not in user_movies[email]:
      user_movies[email].append(row[1][2:-1])

user_movies_public = {}
with open('imdb-2.csv', mode='r') as infile:
  reader = csv.reader(infile)
  for row in reader:
    email = row[0].strip()
    if email not in user_movies_public:
      user_movies_public[email] = []
    if row[1][2:-1] not in user_movies_public[email]:
      user_movies_public[email].append(row[1][2:-1])


for user, us_mov in user_movies.items():
  print(user, len(us_mov))

for user, us_mov in user_movies_public.items():
  print(user, len(us_mov))

my_movies = user_movies_public["cosmin.rusu@epfl.ch"]
print(my_movies)

movie_to_salt = {}
salt_to_movie = {}
for salt, movie in zip(com_dict_sorted, imdb_dict_sorted):
  movie_to_salt[movie[0]] = salt[0]
  salt_to_movie[salt[0]] = movie[0]


my_user_salt = ''

for user, us_mov in user_movies.items():
  ok = True
  for movie in my_movies:
    if movie_to_salt[movie] not in us_mov:
      ok = False
      break
  if ok:
    my_user_salt = user

print(my_user_salt)

with open('com402-2.csv', mode='r') as infile:
  reader = csv.reader(infile)
  for row in reader:
    key = row[1][2:-1]
    if row[0] == my_user_salt:
      print(salt_to_movie[key])





