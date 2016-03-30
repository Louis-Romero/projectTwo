from PIL import Image
import functions

def decryptImage(imagepath):
	#Opens image with hidden text
	imageWithText = Image.open(imagepath)
	pixel = imageWithText.load()
	width, height = imageWithText.size

	outputfile = open('hiddenText.txt', 'w')

	#This loop grabs every pixel in the selected image and creates a list of every pixel's
	#RGB values in binary.
	loopInformation = []
	for x in range(0, 12):	#number of pixels
		for y in range(0, 1):
			redValue, greenValue, blueValue = imageWithText.getpixel((x, y))
			binaryRed = functions.makeNumberBinary(redValue)
			binaryGreen = functions.makeNumberBinary(greenValue)
			binaryBlue = functions.makeNumberBinary(blueValue)
			loopInformation.append(binaryRed)
			loopInformation.append(binaryGreen)
			loopInformation.append(binaryBlue)

	counter = 0
	stringOfBits = ""
	listPixelsAndRowNeeded = []
	for ix in range(0, len(loopInformation)):
		stringOfBits += loopInformation[ix][7]
		counter += 1
		if(counter == 18):
			listPixelsAndRowNeeded.append(stringOfBits)
			stringOfBits = ""
			counter = 0

	pixels = functions.make18BitsANumber(listPixelsAndRowNeeded[0])
	rows = functions.make18BitsANumber(listPixelsAndRowNeeded[1])

	pixels -= 12
	counter = 0
	startingWidth = 12
	listOfRGBValues = []
	for y in range(0, rows): #height
		
		for x in range(startingWidth, width): 	#width needs to be 495 or width
			redValue, greenValue, blueValue = imageWithText.getpixel((x, y))
			binaryRed = functions.makeNumberBinary(redValue)
			binaryGreen = functions.makeNumberBinary(greenValue)
			binaryBlue = functions.makeNumberBinary(blueValue)
			listOfRGBValues.append(binaryRed)
			listOfRGBValues.append(binaryGreen)
			listOfRGBValues.append(binaryBlue)
			counter += 1
			if(pixels == counter):
				break	
		if(y == 0):
			startingWidth = 0

	listOfLeastSignificantBits = []
	#This loop grabs every list significant bit from every pixel's RGB binary value.  
	for ix in range(0, len(listOfRGBValues)):		
		listOfLeastSignificantBits.append(listOfRGBValues[ix][7])
		
	counterOfBits = 0
	newList = []
	stringOfEightBits = ""
	for jx in range(0, len(listOfLeastSignificantBits)):
		stringOfEightBits += listOfLeastSignificantBits[jx]
		counterOfBits += 1
		if(counterOfBits == 8):
			newList.append(stringOfEightBits)
			counterOfBits = 0
			stringOfEightBits = ""

	listOfBinaryAsNumbers = []
	for kx in range(0, len(newList)):
		binaryAsNumber = functions.makeBinaryANumber(newList[kx])
		outputfile.write(chr(binaryAsNumber))

	outputfile.close()
	print "COMPLETE"
