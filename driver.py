#http://pillow.readthedocs.org/en/3.1.x/handbook/tutorial.html
#http://stackoverflow.com/questions/11064786/get-pixels-rgb-using-pil 
#https://docs.python.org/2/tutorial/modules.html
#use a png
from PIL import Image
import functions
import copy

originalImage = Image.open("1.png")
pixel = originalImage.load()
width, height = originalImage.size

wordsFromFile = functions.openFileReadText()
binaryListOfWords = functions.makeBinaryListOfWords(wordsFromFile)

listOfBitsToHide = []

for binaryWord in binaryListOfWords:
	for bit in binaryWord:
		listOfBitsToHide.append(bit)

functions.printList(listOfBitsToHide)

if(len(listOfBitsToHide) % 3):
	numberOfPixelsNeeded = (len(listOfBitsToHide) / 3) + 1
else: 
	numberOfPixelsNeeded = len(listOfBitsToHide) / 3

listOfRGBValues = []

for y in range(0, 1):
	for x in range(0, numberOfPixelsNeeded):
		redValue, greenValue, blueValue = originalImage.getpixel((x, y))
		binaryRed = functions.makeNumberBinary(redValue)
		binaryGreen = functions.makeNumberBinary(greenValue)
		binaryBlue = functions.makeNumberBinary(blueValue)
		print "red " + str(redValue) + " green " + str(greenValue) + " blue " + str(blueValue)
		listOfRGBValues.append(binaryRed)
		listOfRGBValues.append(binaryGreen)
		listOfRGBValues.append(binaryBlue)

functions.printList(listOfRGBValues)

binaryListOfHiddenTextInPixels = []

print "hello"
stringOfHiddenBits = ""

for ix in range(0, len(listOfBitsToHide)):
	for jx in range (0, 7):
		stringOfHiddenBits += listOfRGBValues[ix][jx]
		
	stringOfHiddenBits += listOfBitsToHide[ix]
	binaryListOfHiddenTextInPixels.append(stringOfHiddenBits)
	stringOfHiddenBits = ""

functions.printList(binaryListOfHiddenTextInPixels)