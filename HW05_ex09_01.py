#!/usr/bin/env python3
# HW05_ex09_01.py

# Write a program that reads words.txt and prints only the
# words with more than 20 characters (not counting whitespace).
##############################################################################
# Imports

# Body
def read_check_words():
	"""This method reads a file and prints words > 20 chars"""
	try:
		words_file = open("words.txt")
	except:
		print("Something went wrong")
		return

	for line in words_file:
		words = line.strip()
		if len(words) > 20:
			print(words)


##############################################################################
def main():
    read_check_words()

if __name__ == '__main__':
    main()
