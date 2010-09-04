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

