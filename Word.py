#!/usr/bin/env python

import random

class Word:
	# The actual word this is
	__main_word__ = ""
	# Times the word was used
	__usage_count__ = 0
	# List of related words
	__related_words__ = []
	# Related adjectives
	__adjectives__ = []
	# A list of words that can come before this word
	__pre_words__ = []
	# A list of words that can come after this word
	__post_words__ = []

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

	def getWord():
		return self.__main_word__

	def increaseUsage():
		self.__usage_count__ += 1

	def getUsage():
		return self.__usage_count__

	def addRelated(word):
		for i in self.__related_words__:
			if i == word:
				return

		self.__related_words__.append(word)

	def getRelated():
		el = random.randint(0, len(self.__related_words__))
		return self.__related_words__[el]

	def addAdjective(word):
		for i in self.__adjectives__:
			if i == word:
				return

		self.__adjectives__.append(word)

	def getAdjective():
		el = random.randint(0, len(self.__adjectives__))
		return self.__adjectives__[el]

	def addPostWord(word):
		for i in self.__post_words__:
			if i == word:
				return

		self.__post_words__.append(word)

	def getPostWord():
		el = random.randint(0, len(self.__post_words__))
		return self.__post_words__[el]

	def addPreWord(word):
		for i in self.__pre_words__:
			if i == word:
				return

		self.__pre_words__.append(word)

	def getPreWord():
		el = random.randint(0, len(self.__pre_words__))
		return self.__pre_words__[el]

