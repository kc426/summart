#!/usr/bin/env python
# -*- coding: utf-8 -*-

import summartUtil
from Word import Word
import markov
import sys

DEBUG = True 

# Words to not type
BLACK_LIST = [ "the", "has", "hasn't", "have", "havn't", "a", "an", "is", "it", "to", "its" ]

start = Word(None)

def getWordType(sentence, type):
	types = []
	skip = False

	for i in sentence:
		for j in BLACK_LIST:
			if i == j:
				skip = True

		if summartUtil.getWordFunction(i) == type and skip != True:
			types.append(i)

	return types

def analyze_sentence(sentence):
	related = getWordType(sentence, "noun")
	related.append(getWordType(sentence, "verb"))
	adjectives = getWordType(sentence, "adjective")

def main():	
	text = ""
	option = int(raw_input("1. URL, 2. plain text:"))
	if option == 1:
		if DEBUG:
			url = "http://www.cs.drexel.edu/~jpopyack/Kasparov.html"
		else:
			url = raw_input("Enter the URL: ")
		text = summartUtil.getHtmlText(url)
	elif option == 2:
		filename = raw_input("Enter the filename: ")
		fin = file( filename )
		for line in fin:
			text += line + '\n'
		fin.close()
	else:
		print "Please enter the right option"
		sys.exit(2)

	if DEBUG:
		MAXGEN = 200
	else:
		MAXGEN = int(raw_input("Enter number of words you want to summarize: "))
	
	# start analyze
	sentences = summartUtil.getSentences(text)
	for s in sentences:
		analyze_sentence(s)

if __name__ == "__main__":
	main()
