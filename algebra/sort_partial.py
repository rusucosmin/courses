import urllib2
import operator
import os
from bs4 import BeautifulSoup


class Student:
	def __init__(self, name, grade):
		self._name = name
		self._grade = grade

	def __repr__(self):
		return self._name + " " + str(self._grade)

if not os.path.exists('partial.html'):
	response = urllib2.urlopen('https://docs.google.com/spreadsheets/d/1We7B7CbRNWxnR-BrO1t7Dq7J-wDL0MssIBl7tHO-9hc/pubhtml#')
	f = open('partial.html', 'w')
	f.write(response.read())
	
with open('partial.html', 'r') as f:
	html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.parser')

div_tag = soup.find_all('div', id = "1864821402")

div_soup = BeautifulSoup(str(div_tag[0].contents), 'html.parser')

empty_cells = div_soup.find_all("td", class_="s5")

for emptycell in empty_cells:
	emptycell['class'] = "s4"

empty_cells = div_soup.find_all("td", class_="s3")

for emptycell in empty_cells:
	emptycell['class'] = "s2"

empty_cells = div_soup.find_all("td", class_="s10")

for emptycell in empty_cells:
	emptycell['class'] = "s2"

empty_cells = div_soup.find_all("td", class_="s11")

for emptycell in empty_cells:
	emptycell['class'] = "s4"

all_names = div_soup.find_all("td", class_="s2")
all_grades = div_soup.find_all("td", class_="s4")

all_names = [name for name in all_names if name.getText() != ""]
all_grades = [grade for grade in all_grades if grade.getText() not in ["Pb1", "Pb2", "Pb3", "Pb4", "Total"]]

names = []
grades = []

for i in range(0, len(all_names), 2):
	names.append(all_names[i].getText() + " " +  all_names[i + 1].getText())

for i in range(4, len(all_grades), 5):
	if all_grades[i].getText() == "":
		grades.append(0)
	else:
		grades.append(int(all_grades[i].getText()))

assert(len(grades) == len(names))

students = []
for i in range(min(len(grades), len(names))):
	students.append(Student(names[i], grades[i]))

students = sorted(students, key = operator.attrgetter('_grade'), reverse=True)

with open("main.html", 'w') as f:
	cnt = 0
	for student in students:
		cnt += 1
		line = str(cnt) + " " + student._name + " " + str(student._grade) + '<br>'
		f.write(line.decode('unicode-escape').encode('utf-8'))
		f.write('\n')

with open("main.html", 'r') as f:
	print(f.read())

