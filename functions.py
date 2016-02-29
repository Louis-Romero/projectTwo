#https://docs.python.org/2/tutorial/inputoutput.html
#https://docs.python.org/2/library/functions.html
#https://docs.python.org/2/library/stdtypes.html
#use ord() to get ascii value
#http://www.greenteapress.com/thinkpython/thinkpython.pdf 

#This function accepts an ASCII value and returns the binary string of that ASCII value
def openFileReadText():
	fileWithText = open('words.txt', 'r')
	listOfWords = [] #Contains every word in text file
	fileContent = fileWithText.read()
	listOfWords = fileContent.split()
	return listOfWords

def makeBinaryListOfWords(wordList):
	oneWordInBinary = ""
	wordsFromFileInBinary = []
	for ix in range(0, len(wordList)):
		word = wordList[ix]
		for jx in range(0, len(word)):
			oneWordInBinary += makeNumberBinary(ord(word[jx]))
		wordsFromFileInBinary.append(oneWordInBinary)
		oneWordInBinary = "" #clears word
	return wordsFromFileInBinary
	

def makeNumberBinary(number):
	binaryString = ""
	baseTwoValues = [128, 64, 32, 16, 8, 4, 2, 1] 
	for ix in range(0, 8):
			if(number < baseTwoValues[ix]):
				binaryString += "0"
			else:
				binaryString += "1"
				number -= baseTwoValues[ix]
	return binaryString

def printList(listOfWords):
	for ix in range(0, len(listOfWords)):
		print listOfWords[ix]
