salt_email = "1e698bd5135c4e0321b40c8842bb0f8b9217ffdd3ca1e56d5b9ac5abbbb3136c"

d = {}
with open('imdb-1.csv', 'r') as f:
  for line in f.readlines():
    sp = line.split(',')
    movie = sp[1]
    date = sp[2].strip()
    rating = sp[3].strip()
    if date + "," + rating in d:
      d[date + "," + rating].append(movie)
    else:
      d[date + "," + rating] = [movie]

mov_d = {}
with open('com402-1.csv', 'r') as f:
  for line in f.readlines():
    sp = line.split(',')
    salt_movie = sp[1]
    date = sp[2].strip()
    rating = sp[3].strip()
    k = date + ',' + rating
    if k in d and len(d[k]) == 1:
      mov_d[salt_movie] = d[k][0].strip()[1:-1]

with open('com402-1.csv', 'r') as f:
  for line in f.readlines():
    sp = line.split(',')
    if sp[0] == salt_email:
      salt_movie = sp[1]
      print(mov_d[salt_movie])
