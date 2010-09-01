#!/usr/bin/env python
# -*- coding: utf-8 -*-

import summartUtil
from Word import Word
import markov
import sys

DEBUG = True 

# Words to not type
BLACK_LIST = [ "the", "has", "hasn't", "have", "havn't", "a", "an", "is", "it", "to", "its" ]

# The beginning of a sentence
start_sentence = Word(None)
# All the words we know about
dictionary = dict()

def analyze_sentence(sentence):
	noun = []
	verb = []
	adjective = []
	other = []
	previous_word = start_sentence

	for i in sentence.split():
		# See if word exists in our dictionary
		# If not create it
		if dictionary.has_key(i) == True:
			current_word = dictionary["i"]
		else:
			current_word = Word(i)

		# Increase how much the word has been used
		current_word.increaseUsage()

		previous_word.addPostWord(current_word)
		current_word.addPreWord(previous_word)

		skip = False
		for j in BLACK_LIST:
			if i == j:
				skip = True

		func = summartUtil.getWordFunction(i)

		if func == "noun":
			noun.append(current_word)
		elif func == "verb":
			verb.append(current_word)
		elif func == "adjective":
			adjective.append(current_word)
		else:
			other.append(current_word)

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
