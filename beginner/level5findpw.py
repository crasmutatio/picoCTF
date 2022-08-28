#My little program to find the correct password; started with level 4

#Import hashing library
import hashlib

#Get list of possible passwords as provided
pw_file = open('dictionary.txt', 'r')

#Get the hash that was dumped separately and stored in this file
correct_pw_hash = open('level5.hash.txt', 'r').readline().rstrip()

#Cycle through the options and stop at the comparison with the correct password

try:
	for item in range(65535):
		password = pw_file.readline().strip()
		if  (hashlib.md5(str.encode(password)).hexdigest()) == correct_pw_hash:
			print ("Found the correct password: ", password)
except:
	print("Something went wrong, found no password")

pw_file.close()