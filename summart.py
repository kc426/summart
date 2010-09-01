#!/usr/bin/env python
# -*- coding: utf-8 -*-

import summartUtil
import markov
import sys

DEBUG = False 

# Words to not type
BLACK_LIST = [ "the", "has", "hasn't", "have", "havn't", "a", "an", "is", "it", "to", "its" ]

# The beginning of a sentence
start_sentence = Word(None)
# All the words we know about
dictionary = dict()

def analyze_sentence(sentence):
	nouns = []
	verbs = []
	adjectives = []
	previous_word = start_sentence

	for i in sentence:
		# See if word exists in our dictionary
		# If not create it
		if dictionary.has_key(i) == True:
			current_word = dictionary["i"]
		else:
			current_word = Word(i)
			dictionary[i] = current_word

		# Increase how much the word has been used
		current_word.increaseUsage()

		# Link words together as valid words that can be next to
		# eachother
		previous_word.addPostWord(current_word)
		current_word.addPreWord(previous_word)

		previous_word = current_word

		# Check if the word is black listed meaning we don't want
		# any contextual linking
		skip = False
		for j in BLACK_LIST:
			if i == j:
				skip = True
				break

		if skip == True:
			continue

		# Get the word function and add it to a list of that function
		# Since they are in the same sentence even if they aren't next
		# To eachother they are have a connection
		func = getWordFunction(i)

		if func == "noun":
			nouns.append(current_word)
		elif func == "verb":
			verbs.append(current_word)
		elif func == "adjective":
			adjectives.append(current_word)

	for i in nouns:
		

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

if __name__ == "__main__":
	main()
