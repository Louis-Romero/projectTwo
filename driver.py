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

originalImage.show()

wordsFromFile = functions.openFileReadText()
binaryListOfWords = functions.makeBinaryListOfWords(wordsFromFile)

listOfBitsToHide = []
for binaryWord in binaryListOfWords:
	for bit in binaryWord:
		listOfBitsToHide.append(bit)

#functions.printList(listOfBitsToHide)
#print  "number of bits to hide", len(listOfBitsToHide)
#This creates an integer value that will control the loop that creates a list of RGB values needed
if(len(listOfBitsToHide) % 3):
	numberOfPixelsNeeded = (len(listOfBitsToHide) / 3) + 1
else: 
	numberOfPixelsNeeded = len(listOfBitsToHide) / 3
#print  "number of pixels needed", numberOfPixelsNeeded

numberOfRowsNeeded = (numberOfPixelsNeeded/width) + 1;
#print  "number of rows needed", numberOfRowsNeeded

#print "width", width
#print "height", height

listOfRGBValues = []

counter = numberOfPixelsNeeded
#This loop creates a list of the RGB values needed
#print "Original pixel values"
for y in range(0, numberOfRowsNeeded):
	for x in range(0, width):
		if(counter != 0):
			redValue, greenValue, blueValue = originalImage.getpixel((x, y))
			binaryRed = functions.makeNumberBinary(redValue)
			binaryGreen = functions.makeNumberBinary(greenValue)
			binaryBlue = functions.makeNumberBinary(blueValue)
			
			#print "red " + str(redValue) + " green " + str(greenValue) + " blue " + str(blueValue)
			#print "x ", x
			#print "y ", y
			listOfRGBValues.append(binaryRed)
			listOfRGBValues.append(binaryGreen)
			listOfRGBValues.append(binaryBlue)
			counter -= 1
		else:
			break
redValue, greenValue, blueValue = originalImage.getpixel((5, 0))
#print "hello green ", greenValue
#print "hello blue ", blueValue
#print "RGB bit values unchanged"
#functions.printList(listOfRGBValues) #prints RGB values in binary


#print "bits will now be hidden"

binaryListOfHiddenTextInPixels = []
stringOfHiddenBits = ""

#For each iteration this loop creates a string of 8 bits bits 1-7 are from RGB values and bit 8 is the bit that needs to be hidden

for ix in range(0, len(listOfBitsToHide)):
	for jx in range (0, 7):
		stringOfHiddenBits += listOfRGBValues[ix][jx]
		
	stringOfHiddenBits += listOfBitsToHide[ix]
	binaryListOfHiddenTextInPixels.append(stringOfHiddenBits)
	stringOfHiddenBits = ""

#print "Changed!!!!!!!!!!"
#functions.printList(binaryListOfHiddenTextInPixels)

#This loops gets all decimal values of each binary string and creates 	a new list
listOfNewRGBValues = []
for ix in range(0, len(binaryListOfHiddenTextInPixels)):
	listOfNewRGBValues.append(functions.makeBinaryANumber(binaryListOfHiddenTextInPixels[ix]))


#functions.printList(listOfNewRGBValues)

img = Image.new( 'RGB', (width, height), "black") # create a new black image
pixels = img.load() # create the pixel map

#print "Number of Rows ", numberOfRowsNeeded
#print "Number of Pixels ", numberOfPixelsNeeded

otherCounter = numberOfPixelsNeeded
for y in range(0, height):
	for x in range(0, width):
		redValue, greenValue, blueValue = originalImage.getpixel((x, y))
		pixels[x,y] = (redValue, greenValue, blueValue)

summer = 0
for y in range(0, numberOfRowsNeeded):
	for x in range(0, width):
		
		if(otherCounter != 0):
			#print "x ", x
			#print "y ", y
			
			try:
				newRedValue = listOfNewRGBValues[summer]
				finalXValue = x
				finalYValue = y
			except IndexError:
				redValue, greenValue, blueValue = originalImage.getpixel((x, y))
				newRedValue = redValue
				finalXValue = x
				finalYValue = y
			try:
				newGreenValue = listOfNewRGBValues[summer+1]
				finalXValue = x
				finalYValue = y
			except IndexError:
				#print "used except red"
				#print "x ", x
				#print "y ", y
				redValue, greenValue, blueValue = originalImage.getpixel((x, y))
				newGreenValue = greenValue
				finalXValue = x
				finalYValue = y
			try:
				newBlueValue = listOfNewRGBValues[summer+2]
				finalXValue = x
				finalYValue = y
			except IndexError:
				#print "used except blue"
				#print "x ", x
				#print "y ", y
				redValue, greenValue, blueValue = originalImage.getpixel((x, y))	
				#print blueValue
				newBlueValue = blueValue
				finalXValue = x
				finalYValue = y

			#print "Red Value ", newRedValue, "Green Value ", newGreenValue, "Blue Value", newBlueValue
			pixels[x,y] = (newRedValue, newGreenValue, newBlueValue) # set the color accordingly
			otherCounter -= 1
		summer += 3
#print "sup" , x
#print "sup" , y


#print "New RGB Values to hide"
#functions.printList(listOfNewRGBValues)
img.show()