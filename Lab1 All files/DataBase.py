#Database.py file
import re

class tempData: #temperature data, opens and reads raw temp data
    def __init__(self, lines):
        temp = open('Temperature.html', 'r')
        self.lines = temp.readlines()
        for x in range(5):
            del self.lines[0]
        del self.lines[-1]

temp = tempData([])

#the other way to parse the data,
for x in range(len(temp.lines)):
    noHTML = re.sub("<TBODY><TR><TD>", "", temp.lines[x])
    temp.lines[x] = noHTML
    noHTML = re.sub("</TD><TD>", " ", temp.lines[x])
    temp.lines[x] = noHTML
    noHTML = re.sub("</TD></TR></TBODY>", "", temp.lines[x])
    temp.lines[x] = noHTML

#stores all the years into a list
years = []
for x in range(len(temp.lines)):
    years.append(re.search("[0-9]{4}", temp.lines[x]).group())
    noYear = re.sub(years[x], "", temp.lines[x]) #this takes the year out
    temp.lines[x] = noYear

    
temperatures = {}
for x in range(len(temp.lines)):
    temp.lines[x] = re.sub("   ", "", temp.lines[x])
    noSpace = re.split("\s", temp.lines[x])
    del noSpace[-1]
    temperatures[years[x]] = noSpace #sets the year as the key and their respective values
    print(noSpace) 
    
    
