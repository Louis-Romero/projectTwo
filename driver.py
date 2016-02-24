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

#imageToHideText.show()

wordsFromFile = functions.openFileReadText()
binaryListOfWords = functions.makeBinaryListOfWords(wordsFromFile)

#functions.printList(binaryListOfWords)

for binaryWord in binaryListOfWords:
	for bit in binaryWord:
		print bit


#print binaryListOfWords[0][0]
#print binaryListOfWords[0][1]

#print binaryListOfWords[1][2]
#copyOfImage = copy.copy(originalImage)

#for y in range(0, height):
	#for x in range(0, width):
		#redValue, greenValue, blueValue = originalImage.getpixel((y, x))
		#binaryRed = textToascii.convertOneASCIIValueToBinary(redValue)
		#binaryGreen = textToascii.convertOneASCIIValueToBinary(greenValue)
		#binaryBlue = textToascii.convertOneASCIIValueToBinary(blueValue)

		#print "red " + str(redValue) + " green " + str(greenValue) + " blue " + str(blueValue)

		#binaryRed = textToascii.convertOneASCIIValueToBinary(redValue)
		#binaryGreen = textToascii.convertOneASCIIValueToBinary(greenValue)
		#binaryBlue = textToascii.convertOneASCIIValueToBinary(blueValue)
		#print redValue
		#print binaryRed
		#print binaryGreen
		#print binaryBlue