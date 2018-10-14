import os
import filecmp
# from dateutil.relativedelta import *
from datetime import date


def getData(file):
# get a list of dictionary objects from the file
#Input: file name
#Ouput: return a list of dictionary objects where
#the keys are from the first row in the data. and the values are each of the other rows
	
	# open file and clean line
	dataFile = open(file, "r")
	firstLine = dataFile.readline()
	firstLine = firstLine.strip()
	firstLineWordList = firstLine.split(",")
	
	# Assign values to first, last, email, class, and DOB values
	first = firstLineWordList[0]
	last = firstLineWordList[1]
	email = firstLineWordList[2]
	__class = firstLineWordList[3]
	dOB = firstLineWordList[4]
	
	# list for dicts of names and infos
	listOfDicts = []

	# TODO: get the names and emails and classes and DOB into a list
	for line in dataFile:

		# put a line into a dictionary
		roomDict = {}
		line = line.strip()
		lineList = line.split(",")
		roomDict[first] = lineList[0]
		roomDict[last] = lineList[1]
		roomDict[email] = lineList[2]
		roomDict[__class] = lineList[3]
		roomDict[dOB] = lineList[4]

		# add to list of dicts
		listOfDicts.append(roomDict)
	
	return listOfDicts



	

def mySort(data,col):
# Sort based on key/column
#Input: list of dictionaries and col (key) to sort on
#Output: Return the first item in the sorted list as a string of just: firstName lastName
	data = sorted(data, key = lambda name: name[col])
	name = data[0]["First"] + " " + data[0]["Last"] 
	
	return name


def classSizes(data):
# Create a histogram
# Input: list of dictionaries
# Output: Return a list of tuples sorted by the number of students in that class in
# descending order
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]
	counter = dict()
	for item in data:
		counter[item["Class"]] = counter.get(item["Class"], 0) + 1
	
	# convert data to a list of tuples
	counterList = list()
	for key, value in counter.items():
		counterList.append((key, value))

	# sort list of tuples
	counterList.sort(key=lambda tup: tup[1], reverse=True)
	
	return counterList


# TODO: does this work properly? Uncertain if dates are being counted properly
def findMonth(a):
	countItems = dict()
	# create a list of all dates 
	for item in a:
		# convert date items into a list of string numbers
		dateString = item["DOB"]
		dates = dateString.split("/")
		# count dates
		countItems[dates[0]] = countItems.get(dates[0], 0) + 1
	
	# convert dictionary to a list
	sortList = list()
	for key, item in countItems.items():
		sortList.append((key, item))
	
	# sort items into descending order
	sortList.sort(key=lambda item: item[1], reverse=True)
	
	return int(sortList[0][0])
# Find the most common birth month form this data
# Input: list of dictionaries
# Output: Return the month (1-12) that had the most births in the data

# TODO: does this sort properly?
def mySortPrint(a,col,fileName):
	writeFile = open(fileName, 'w')

	# write CSV headers
	writeFile.write("First,Last,Email \n")
	
	# sorts file by col
	a = sorted(a, key=lambda item: item[col])

	for item in a:
		writeFile.write(item["First"] + ',' + item["Last"] + ',' + item["Email"] + "\n")
	
	writeFile.close()
#Similar to mySort, but instead of returning single
#Student, the sorted data is saved to a csv file.
# as fist,last,email
#Input: list of dictionaries, col (key) to sort by and output file name
#Output: No return value, but the file is written

	

def findAge(a):
# def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest
# integer.  You will need to work with the DOB and the current date to find the current
# age in years.

	pass


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()
