# Homework 1

## Ex1

This was easy. I just opened the login form, and tried some
random inputs. Then, since I saw some alerts, I thought I should
open the source code of the webpage to see the script that
generated that alert. There, I found the script that basically
checks if the password is equal to the username encrypted
with the base64 xor method (superencryption). So I just
called that method with my username (cosmin.rusu@epfl.ch)
and got the base64 encoded username which I used as a password.

## Ex2

I was kind of confused with this one because you could basically
enter anything there, so I thought why do I need to provide
my email? Then as I read again the statement it says the Evil
Company is tracking you (so there must be a 🍪 cookie).
Found out the token, decoded from base64, saw there is a `user`
field, changed to `admin`, didn't work, changed to
`administrator` and worked.


## Ex3

This was pretty straight forward. I just followed all the
instructions in the doc. You can simply run the `intercept.py`
file from the src subdir, exactly as explained in the
requirements pdf, using the command:
```
$ python3 intercept.py  # from within the docker container
```

## Ex4

Again, using the same idea as in ex3, I just had to
do some regex matching based on what was explained in the
documents representing the task. Basically I regex
agains the two possible secrets: credit cards and
passwords, and then create a set out of the matches.
When the set reaches 5 elements, I make the request to
the server and print the token.

```
$ python3 ex4.py  # from within the docker container
```

## Ex5


