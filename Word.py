#!/usr/bin/env python

import random

class Word:
	
	# Check if the word is in the dictionary and only add it if it isn't
	def __add_word__(self, dict, word):
		if dict.has_key(word.getWord()):
			return
		else:
			dict[word.getWord()] = word

	# Return a random word from a dictionary
	def __get_rand_word__(self, dict):
		keys = dict.keys()
		try:
			key = random.choice(keys)
		# return None if empty list
		except IndexError:
			return None
		return dict[key]
		
	def __init__(self, main_word = None, grammer = None):
		random.seed()
		# The actual word this is
		self.__main_word__ = main_word
		# Times the word was used
		self.__usage_count__ = 0
		# List of related words
		self.__related__ = {}
		# Related adjectives
		self.__adjectives__ = {}
		# A list of words that can come before this word
		self.__pre__ = {}
		# A list of words that can come after this word
		self.__post__ = {}
		# The type of word it is i.e noun, verb, adjective
		self.__grammer__ = grammer


		self.__main_word__ = main_word
		self.__gramer__ = grammer
		
	def __eq__(self, other):
		if other is not None and self.__main_word__ == other.getWord():
			return True
		else:
			return False

	def __ne__(self, other):
		if other is None or self.__main_word__ != other.getWord():
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

	def writePostDot(self, f):
		for i in self.__post__.keys():
			f.write("\"" + self.getWord() + "\" -> \"" + self.__post__[i].getWord() + "\";\n")

	def addPreWord(self, word):
		self.__add_word__(self.__pre__, word)

	def getPreWord(self):
		return self.__get_rand_word__(self.__pre__)

	def getGrammer(self):
		return self.__grammer__
