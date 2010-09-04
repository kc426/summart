#!/usr/bin/env python
import sys, re
from Word import Word

class Markov:

	def __init__(self, start_word, end_word, start_grammer, end_grammer):
		self.__start_word__ = start_word
		self.__end_word__ = end_word
		self.__start_grammer__ = start_grammer
		self.__end_grammer__ = end_grammer

		self.__wordUsage__ = {}
		self.__original__ = ""
		self.__black_list__ = []

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

	def set_original(self, original):
		self.__original__ = original

	def set_blackList(self, black_list):
		self.__black_list__ = black_list

	def fitness(self, summary):
		punctuation = re.compile(r"[^\w\s]")

		if self.__wordUsage__ == {} or self.__original__ == "":
			#remove punctuation
			self.__original__ = punctuation.sub("", self.__original__)
	
			#counting the usage in the original article
			words = self.__original__.split()
			for word in words:
				word = word.lower()
				if not self.__wordUsage__.has_key(word):
					self.__wordUsage__[word] = 1
				else:
					self.__wordUsage__[word] += 1
	
		# calculating fitness
		score = 0
		summary = punctuation.sub("", summary)
		words = summary.split()
		for word in words:
			word = word.lower()
			if word in self.__black_list__:
				continue
			if self.__wordUsage__.has_key(word):
				score += self.__wordUsage__[word]
				self.__wordUsage__[word] = 0 # repeated words do not again point
		return score

	##
	# @param population list of summary
	def select(self, population, original="", black_list=[])
		if original != "":
			self.__original__ = original
		if black_list != []:
			self.__black_list__ = black_list

		#calcuate fitness for each summary
		#rank = {score: index}
		rank = {}
		i=0
		for summary in population:
			score = fitness(summary)
			if not rank.has_key(score):
				rank[score] = [i]
			else:
				rank[score].append(i)
			i+=1
		bestIndex = max(rank.keys())
		#pick the first one if multiple summary has the same score
		return population[rank[bestIndex]]

		
