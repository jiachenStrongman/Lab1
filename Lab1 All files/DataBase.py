#Database.py file
import re
import sqlite3

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
            noSpace[i] = float(noSpace[i]) #converts to float as it was a string
        temperatures[int(years[x])] = noSpace
        #sets the year as int and as the key and their respective values

class database:
    def __init__(self, tempDatabase): #connect and initialize class function
        self.tempDatabase = sqlite3.connect('temperatures.db')
        cursor = self.tempDatabase.cursor()
        print("Database connected")
        cursor.close()
        if(self.tempDatabase):
            self.tempDatabase.close()
        

    def table(self): #table class function that creates the database table
        self.tempDatabase = sqlite3.connect('temperatures.db')
        tempTable = '''CREATE TABLE tempTable(
                    YEAR INTEGER PROMARY KEY,
                    MEDIAN REAL,
                    UPPER REAL,
                    LOWER REAL);'''
        cursor = self.tempDatabase.cursor()
        cursor.execute(tempTable)
        self.tempDatabase.commit()
        print("table created")
        cursor.close()
        if(self.tempDatabase):
            self.tempDatabase.close()

    def insert(self, year, med, up, low): #insert data function
        self.tempDatabase = sqlite3.connect('temperatures.db')
        cursor = self.tempDatabase.cursor()
        insertTab = '''INSERT INTO tempTable
                    (YEAR, MEDIAN, UPPER, LOWER) VALUES (?, ?, ?, ?)'''
        data_tuple = (year, med, up, low)
        cursor.execute(insertTab, data_tuple)
        self.tempDatabase.commit()
        cursor.close()
        if(self.tempDatabase):
            self.tempDatabase.close()

    def search(self): #retrieves data from specified year
        self.tempDatabase = sqlite3.connect('temperatures.db')
        cursor = self.tempDatabase.cursor()
        cursor.execute('''SELECT YEAR, MEDIAN FROM tempTable''')
        result = cursor.fetchall()
        return result

    def checkTable(self): #checks to see if the table is already there
        self.tempDatabase = sqlite3.connect('temperatures.db')
        cursor = self.tempDatabase.cursor()
        cursor. execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name = 'tempTable' ''')
        if (cursor.fetchone()[0] == 1):
            return False
        else:
            return True
        cursor.close()
        if(self.tempDatabase):
            self.tempDatavase.close()

   

#stores temp data into a dictionary
temp = tempData([])
yearData = []
allTempData = {} #this is where all the data is stored before it goes into the database. Format year: med, up, low
tempParse(temp)
storeYear(temp, yearData)
storeTempData(temp, allTempData, yearData)

#database class
tempDB = database([])
#this is done for my sake, as i keep testing the code and it will keep adding to database if it doesn't check
if(tempDB.checkTable()):
    tempDB.table()
    #mama mia we got ourselves a filled table full of data
    for i in allTempData:
        tempDB.insert(i, allTempData[i][0], allTempData[i][1], allTempData[i][2])



    
