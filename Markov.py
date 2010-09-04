#!/usr/bin/env python
import sys, re
from Word import Word

class Markov:

	def __init__(self, start_word, end_word, start_grammer, end_grammer):
		self.__start_word__ = start_word
		self.__end_word__ = end_word
		self.__start_grammer__ = start_grammer
		self.__end_grammer__ = end_grammer

	def GenerateSentence(self):
		sentence = ""
		current_word = self.__start_word__

		if None not in [current_word, self.__end_word__]:
			while current_word != self.__end_word__:
				current_word = current_word.getPostWord()
				if current_word == None:
					continue
				sentence = sentence + " " + current_word.getWord()

		return sentence

	def GenerateSummary(self, length):
		summary = []

		for i in range(length):
			summary.append(self.GenerateSentence())

		return summary

	def fitness(original, summary="", black_list=[]):
		wordUsage = {}
		#remove punctuation
		punctuation = re.compile(r"[^\w\s]")
		original = punctuation.sub("", original)
	
		#counting the usage in the original article
		words = original.split()
		for word in words:
			word = word.lower()
			if not wordUsage.has_key(word):
				wordUsage[word] = 1
			else:
				wordUsage[word] += 1
		print wordUsage
	
		# calculating fitness
		score = 0
		summary = punctuation.sub("", summary)
		words = summary.split()
		for word in words:
			word = word.lower()
			if word in black_list:
				continue
			if wordUsage.has_key(word):
				score += wordUsage[word]
				wordUsage[word] = 0 # repeated words do not again point
		return score
