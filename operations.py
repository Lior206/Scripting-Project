#! /usr/bin/python3

from os import listdir, remove
import subprocess
from encrypt import *

#------------ task operations--------------------	

def extractDirPath(path):
	if decideTypeOfPath(path) == "File":
		return "/".join(path.split("/")[0:-1])
	else:
		return path
		
def executePythonFile(path):
	subprocess.call(f'python3 /{path}', shell=True)
	
	
def decideTypeOfPath(path):
	splitList = path.split(".")
	if len(splitList) == 1:
		return "Dir"
	elif len(splitList) == 2:
		return "File"
	else:
		return "None"	
		
		
def newfileName(path, typeOfFile):
	newFileName = path.split("/")[-1].split(".")[0] + typeOfFile
	if len(path.split('/')) == 1:
		return newFileName
	else:
		return "/".join(path.split('/')[:-1]) + '/' + newFileName

	
def encryptFile(path):
	with open(path, 'r') as fileToEncrypt:
		codeToEncrypt = fileToEncrypt.read()
		with open(newfileName(path, ".txt"), 'a') as encryptFile:
			encryptedStr = encryptCode(codeToEncrypt)
			encryptFile.write(encryptedStr)
	remove(path)


def decodeFile(path):
	with open(path, 'r') as fileToDecode:
		codeToDecode = fileToDecode.read()
		with open(newfileName(path, ".py"), 'a') as decodeFile:
			decodedStr = decodeCode(codeToDecode)
			decodeFile.write(decodedStr)
	remove(path)


def encryptDir(path):
	dirContentList = listdir(path)
	if len(dirContentList) == 0:
		return
		
	for obj in dirContentList:
		if obj != "__pycache__":
			if decideTypeOfPath(obj) == "File":
				encryptFile(path + '/' + obj)
			else:
				encryptDir(path + '/' + obj)
			

	
def decodeDir(path):
	dirContentList = listdir(path)
	if len(dirContentList) == 0:
		return
		
	for obj in dirContentList:
		if obj != "__pycache__":
			if decideTypeOfPath(obj) == "File":
				decodeFile(path + '/' + obj)
			else:
				decodeDir(path + '/' + obj)


def runEncFile(path):
	typeOfPath = decideTypeOfPath(path)
	if typeOfPath == "Dir":
		print("Should etered a Path to a txt(python) file!")
	else:
		dirFilePath = extractDirPath(path)
		decodeDir(dirFilePath)
		executePythonFile(newfileName(path, ".py"))
		encryptDir(dirFilePath)
	
		
		
