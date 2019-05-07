#!/usr/bin/env python3

import sys
import random
import datetime
import csv

from random import randrange, randint
import numpy as np
import scipy as sp

date_start = datetime.date(2000, 1, 1)
date_period = 365 * 17
noise_cache = {}

# Reads in emails.txt and movies.txt and creates 'num_movies' entries for each
# email.
# Returns the database for testing purposes, the emails and the movies
def create_db(num_movies):
    with open("emails.txt") as f:
        emails = f.read().split("\n")
    while "" in emails:
        emails.remove("")

    with open("movies.txt") as f:
        movies = f.read().split("\n")
    while "" in movies:
        movies.remove("")

    db = []

    for email in emails[:3]:
        movies_index = list(range(0, len(movies)))
        random.shuffle(movies_index)
        for i, f in enumerate(movies_index[0:num_movies]):
            dat = date_start + datetime.timedelta(randint(1, date_period))
            db.append([email, movies[f], dat, randint(1, 5)])

    return db, emails, movies


def count_ratings(db, movies, rating_levels):
    k = len(movies)
    assert len(movies) == len(rating_levels) == k

    epsilon = np.log(2) / k
    lap_scale = 1 / epsilon

    q_ids = [movie + str(rating) for movie, rating in zip(movies, rating_levels)]

    for m, r in zip(movies, rating_levels):
      q_id = m + str(r)

      if q_id in noise_cache:
        continue

      contor = 0
      for i in range(len(db)):
        if db[i][1] == m and db[i][3] >= r:
          contor += 1

      noise_cache[q_id] = np.random.laplace(contor, lap_scale)

    return [noise_cache[q_ids[x]] for x in range(k)]


if __name__ == "__main__":
    if len(sys.argv) == 1:
        # You can change this part to test the queries as you like.
        print("Testing mode")
        db, emails, movies = create_db(2)
        print("------------")
        queried_movies = movies[:5]
        queried_rating_levels = np.random.randint(1, high=5, size=5)
        results = count_ratings(db, queried_movies, queried_rating_levels)
        print("Queried movies:", queried_movies)
        print("Queried rating levels:", queried_rating_levels)
        print("Response:", results)

    else:
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # !! Do not modify this part !!
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        db_file = sys.argv[1]
        with open(db_file) as f:
            db = list(csv.reader(f, skipinitialspace=True))

        # Get nice ints for comparisons
        for i, line in enumerate(db):
            db[i][3] = int(line[3])

        movies, rating_levels = sys.argv[2:4]
        movies = movies.split('|')
        rating_levels = [int(x) for x in rating_levels.split(',')]
        result = count_ratings(db, movies, rating_levels)

        with open("/tmp/student.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerows([result])

