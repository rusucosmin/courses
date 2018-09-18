#Lab02 - Grep / Sed / Awk

###Practice Problems

My solution for the practice problems from this [link](http://www.cs.ubbcluj.ro/~rares/course/os/res/gsa/gsa.html).
1.  Find all the usernames that logged in from "economica" on a Sunday
    `cat last.fake | grep "economica" | grep "Sun" | awk '{print $1}' | sort | uniq`

4.  Display all the distinct TTYs used by user root.
    `cat ps.fake | grep "^root" | awk '{print $6}' | sort | uniq`

###Grep

###Sed
- Some useful links:
    - [From lab](https://www.cs.ubbcluj.ro/~alinacalin/SO/SED.txt)
