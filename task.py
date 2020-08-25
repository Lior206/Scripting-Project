#! /usr/bin/python3

from oparations import *
	
				
def commitTask(task, path):
	printCommitedMessege = True
	print(f"Commiting Task {task} reaching {path}")
	typeOfPath = decideTypeOfPath(path)
	if task == "-en":
		if typeOfPath == "File":
			print("Encrypting File...")
			encryptFile(path)
		elif typeOfPath == "Dir":
			print("Encrypting Directory...")
			encryptDir(path)
		else:
			print("Invalid Path")
	elif task == "-de":
		if typeOfPath == "File":
			print("Decode File...")
			decodeFile(path)
		elif typeOfPath == "Dir":
			print("Decode Directory...")
			decodeDir(path)
		else:
			print("Invalid Path")
	elif task == "-r":
		runEncFile(path)
	else:
		printCommitedMessege = False
		print("Invalid Argument")
	if printCommitedMessege:
		print("Task Commited!")
		
		

