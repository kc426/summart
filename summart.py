#!/usr/bin/env python
# -*- coding: utf-8 -*-

import summartUtil
from Word import Word
from Markov import Markov
import sys

DEBUG = True 

# Words to not type
BLACK_LIST = [ "the", "has", "hasn't", "have", "havn't", "a", "an", "is", "it", "to", "its" ]

# The grammer a sentence can start with
start_grammer = Word(' ')
# The grammer a sentence can end with
end_grammer = Word('.')
# All the grammer we know about
grammer_dictionary = {start_grammer.getWord():start_grammer, end_grammer.getWord():end_grammer}
# The words that can start a sentence
start_word = Word(' ', start_grammer)
# The words that can end a sentence
end_word = Word('.', end_grammer)
# All the words we know about
word_dictionary = {start_word.getWord():start_word, end_word.getWord():end_word}

def analyze_sentence(sentence):
	sentence = sentence.strip()
	if sentence == '':
		return
	nouns = []
	verbs = []
	adjectives = []
	current_word = start_word
	current_grammer = start_grammer
	previous_word = start_word
	previous_grammer = start_grammer

	for i in sentence.split():
		# See if word exists in our dictionary
		# If not create it
		if word_dictionary.has_key(i) == True:
			current_word = word_dictionary[i]
			current_grammer = current_word.getGrammer()
		else:
			# Get the grammer
			grammer = summartUtil.getWordFunction(i)

			# See if that grammer type exists, if not create it
			if grammer_dictionary.has_key(grammer) == True:
				current_grammer = grammer_dictionary[grammer]
			else:
				current_grammer = Word(grammer)
				grammer_dictionary[grammer] = current_grammer

			current_word = Word(i, current_grammer)
			word_dictionary[i] = current_word

		# Increase how much the word and grammer have been used
		current_word.increaseUsage()
		current_grammer.increaseUsage()

		# Link words together as valid words that can be next to
		# eachother
		previous_word.addPostWord(current_word)
		current_word.addPreWord(previous_word)

		previous_grammer.addPostWord(current_grammer)
		current_grammer.addPreWord(previous_grammer)

		previous_word = current_word
		previous_grammer = current_grammer

		# Check if the word is black listed meaning we don't want
		# any contextual linking
		if i in BLACK_LIST:
			continue

		# Link the context based on what type of word it is
		if current_word.getGrammer().getWord() == "noun":
			nouns.append(current_word)
		elif current_word.getGrammer().getWord() == "verb":
			verbs.append(current_word)
		elif current_word.getGrammer().getWord() == "adjective":
			adjectives.append(current_word)

	current_word.addPostWord(end_word)
	end_word.addPreWord(current_word)
	current_grammer.addPostWord(end_grammer)
	end_grammer.addPreWord(current_grammer)

	for i in nouns:
		current_word = i
		for j in nouns:
			if i == j:
				continue

			current_word.addRelated(j)

		for j in verbs:
			current_word.addRelated(j)
			j.addRelated(current_word)

		for j in adjectives:
			current_word.addAdjective(j)
			j.addRelated(current_word)

# Generate a dot file so its easier to visualize what is going on
# Each word in the dot file will have links to all valid post words
# Empty is the start of a sentence while . is the end of a sentence
# To convert from dot file to a png make sure you have graphviz installed
# and do
# dot -Tpng -o word.png word.dot
def outputDot(filename, dict):
	f = open(filename, 'w')
	f.write("digraph dictionary {\n")

	for i in dict.keys():
		dict[i].writePostDot(f)

	f.write("}\n")
	f.close()

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

	MAXGEN = int(raw_input("Enter number of population: "))
	
	sentences = summartUtil.getSentences(text)
	print "Analyzing text..."
	for s in sentences:
		analyze_sentence(s)

	# Generate graph with
	# dot -Tpng -o test.png test.dot
	outputDot("word.dot", word_dictionary)
	outputDot("grammer.dot", grammer_dictionary)

	markov = Markov(start_word, end_word, start_grammer, end_grammer)
	markov.set_original(text)
	markov.set_blackList(BLACK_LIST)

	print "Generating summary..."
	#print markov.GenerateSentence()
	
	population = markov.GenerateSummary(MAXGEN)
	print markov.select(population)


if __name__ == "__main__":
	main()
