#!/usr/bin/env python

class Word:
	# The actual word this is
	__main_word__ = ""
	# Times the word was used
	__usage_count__ = 0
	# List of related words
	__related_words__ = []
	# A list of words that can come before this word
	__pre_words__ = []
	# A list of words that can come after this word
	__post_words__ = []
	# A dictionary of all known words
	__known_words__

	def __init__(self, main_word, known_words):
		self.__main_word__ = main_word
		self.__known_words__ = known_words

	def getWord():
		return self.__main_word__

	def increaseUsage():
		self.__usage_count__++

	def getUsage():
		return self.__usage_count__

	def addRelated(word):
		print "Add a related word to the related list"

	def getRelated():
		
