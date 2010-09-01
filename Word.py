#!/usr/bin/env python

import random

class Word:
	# The actual word this is
	__main_word__ = ""
	# Times the word was used
	__usage_count__ = 0
	# List of related words
	__related__ = dict()
	# Related adjectives
	__adjectives__ = dict()
	# A list of words that can come before this word
	__pre__ = dict()
	# A list of words that can come after this word
	__post__ = dict()

	# Check if the word is in the dictionary and only add it if it isn't
	def __add_word__(self, dict, word):
		if dict.has_key(word.getWord()):
			return
		else:
			dict[word.getWord()] = word

	# Return a random word from a dictionary
	def __get_rand_word__(self, dict):
		list = dict.values()
		element = random.randint(0, len(list))
		return self.list[element]
		
	def __init__(self, main_word):
		random.seed()
		self.__main_word__ = main_word

	def __eq__(self, other):
		if self.__main_word__ == other.getWord():
			return True
		else:
			return False

	def __ne__(self, other):
		if self.__main_word__ != other.getWord():
			return True
		else:
			return False

	def getWord(self):
		return self.__main_word__

	def increaseUsage(self):
		self.__usage_count__ += 1

	def getUsage(self):
		return self.__usage_count__

	def addRelated(self, word):
		self.__add_word__(self.__related__, word)

	def getRelated(self):
		return self.__get_rand_word__(self.__related__)

	def addAdjective(self, word):
		self.__add_word__(self.__adjectives__, word)

	def getAdjective(self):
		return self.__get_rand_word__(self.__adjectives__)

	def addPostWord(self, word):
		self.__add_word__(self.__post__, word)

	def getPostWord(self):
		return self.__get_rand_word__(self.__post__)

	def addPreWord(self, word):
		self.__add_word__(self.__pre__, word)

	def getPreWord(self):
		return self.__get_rand_word__(self.__pre__)

