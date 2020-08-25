#! /usr/bin/python3


#------------ encryption--------------------
	
def convertToSevenDigStr(number):
	numberLengh = len(number)
	if numberLengh < 7:
		number = (7-numberLengh)*'0' + number
	return number


def xorFunction(binaryStr, mask):
	res = ''
	binMask = convertToSevenDigStr(format(ord(mask), 'b'))
	for index in range(len(binaryStr)):
		addition = int(binMask[index]) + int(binaryStr[index])
		if addition == 1:
			res += "1"
		else:
			res += "0"
	return res
	
		
def cipherLockKeyFunction(binaryStr):
	return xorFunction(binaryStr, 'L')
	
			
def encryptCode(code):
	result = ''
	for letter in code:
		result += cipherLockKeyFunction(convertToSevenDigStr(format(ord(letter), 'b')))
	return result.replace("1", "/").replace("0", "_")	
	


def decodeCode(code):
	binStr = code.replace("/", "1").replace("_", "0")
	listOfBin = [cipherLockKeyFunction(binStr[i:i+7]) for i in range(0, len(binStr), 7)]
	listOfChar = [chr(int(listOfBin[i], base=2)) for i in range(0, len(listOfBin))]
	return "".join(listOfChar)


