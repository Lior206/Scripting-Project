#! /usr/bin/python3

import sys
from task import commitTask

def displayMenuFunc():
	print("""Welcome to Cipher
______________________________________________________
 
    _______  _____  ________   __  __  ______  _______
    | _____| |_  _| |  ___  | | | | | | ____| | ___  |
    | |        ||   |  |__| | | |_| | | |___  | |__| | 
    | |        ||   |  _____| |  _  | |  ___| | _____|
    | |____   _||_  | |       | | | | | |___  | |\ \  
    |______| |____| |_|       |_| |_| |_____| |_| \_\\

______________________________________________________


-en + path/file  ====> encypte file
-de + path/file  ====> decode file
-r + path/en_file ====> run encrypted file""")

def displayArguError():
	print("Not enuogh argument!")
	print("Should be like ====> cyper -en path/file")

if len(sys.argv) == 1:
	displayMenuFunc()
elif len(sys.argv) == 2:
	displayArguError()
elif len(sys.argv) == 3:
	commitTask(sys.argv[1], sys.argv[2])
else:
	print("To many arguments")
