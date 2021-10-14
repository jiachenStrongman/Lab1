#Database.py file
import re

class tempData:
    #temperature data, opens and reads raw temp data
    def __init__(self, lines):
        temp = open('Temperature.html', 'r')
        self.lines = temp.readlines()
        for x in range(5):
            del self.lines[0]
        del self.lines[-1]

def tempParse(tempFile):
    #the other way to parse the data,
    for x in range(len(tempFile.lines)):
        #remove all of the html tags in the file to leave just the data
        noHTML = re.sub("<TBODY><TR><TD>", "", tempFile.lines[x])
        tempFile.lines[x] = noHTML
        noHTML = re.sub("</TD><TD>", " ", tempFile.lines[x])
        tempFile.lines[x] = noHTML
        noHTML = re.sub("</TD></TR></TBODY>", "", tempFile.lines[x])
        tempFile.lines[x] = noHTML
        
def storeYear(tempFile, years):
    #stores all the years into a list
    for x in range(len(tempFile.lines)):
        years.append(re.search("[0-9]{4}", tempFile.lines[x]).group())
        noYear = re.sub(years[x], "", tempFile.lines[x])
        #this takes the year out
        tempFile.lines[x] = noYear

def storeTempData(tempFile, temperatures, years):
    #stores complete data into dictionary
    for x in range(len(tempFile.lines)):
        tempFile.lines[x] = re.sub("   ", "", tempFile.lines[x])
        noSpace = re.split("\s", tempFile.lines[x])
        del noSpace[-1]
        for i in range(3):
            noSpace[i] = float(noSpace[i])
            #converts data from string to float
        temperatures[int(years[x])] = noSpace
        #sets the year as int and as the key and their respective values

#test to make sure all functions are working
temp = tempData([])
yearData = []
allTempData = {}

tempParse(temp)

storeYear(temp, yearData)

storeTempData(temp, allTempData, yearData)

print(allTempData[1998])
#test to make sure all functions are working 
    
    
