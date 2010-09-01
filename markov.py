#!/usr/bin/python
# -*- coding: utf-8 -*-
# markov.py - learn from input file(s), produce some fun output.
#		Uses 2-word prefixes
#
#	Adapted from markov.pl:
#		Copyright (C) 1999 Lucent Technologies
#		Excerpted from 'The Practice of Programming'
#		by Brian W. Kernighan and Rob Pike
#
# Kurt Schmidt
#	7/06
#
# EDITOR:  tabstop=2
#


import sys
import random
from Word import Word

MAXGEN = 300;	# max # of words to output
STARTWORD = "start word";	# sentinel

MAX_LINE_LEN = 76	# for output only
	# note, a single string > 76 chars will not be broken



########   BUILD TABLE   #############

def build( istream, table ) :
	"""Given an istream file and a hash table, reads istream, 
	Returns the # of words inserted into table"""

	rV = 0

	for l in istream :			# grab a line
		current_word = Word(None)
		previous_word = Word(None)
		
		l = l.strip()
		for tok in l.split() :		# grab each word (with pumctuation and caps)
			rV += 1
			if len(table) <= 0:
				table[STARTWORD] = Word(tok)
			elif table.has_key(tok):
				current_word = table[tok]
			else:
				current_word = Word(tok)
				table[tok] = current_word

			# Increase how much the word has been used
			current_word.increaseUsage()

			# Link words together as valid words that can be next to
			# eachother
			previous_word.addPostWord(current_word)
			current_word.addPreWord(previous_word)

			previous_word = current_word
	return rV
	


######   GENERATE TEXT   ####################

def generate( table, MAXGEN ) :
	line = ""	# to accumulate words, print a line at a time
	current_word = STARTWORD

	for i in range( MAXGEN ) :
		current_word_O = table[current_word]
		 
			# choose a suffix from the list
		word = random.choice( current_word_O.getPostWord() )

		#if suf == NONWORD :	# caught our "end story" marker.  Get out
		#	if len( line ) > 0 :
		#		print line
		#	break
		#if len( line ) + len( suf ) > MAX_LINE_LEN :
		#	print line
		#	line = ""
		line = line + " " + word.getPostWord()

		current_word = word.getPostWord
	# print until it sees the last period
	periodIndex = line.rfind('.')+1
	print line[:periodIndex]

def main( argv = sys.argv ) :

	random.seed()

	table = {}

	sys.argv.pop( 0 )	# get rid of script name

	if len( sys.argv ) == 0 :
		build( sys.stdin, table )
	else :
		for f in sys.argv :		# iterate over files
			fin = open( f, "r" )
			build( fin, table )
			fin.close()
	
	generate( table, MAXGEN )


# check to see if we are being called explicitly, or imported
if __name__ == "__main__" :
	sys.exit( main() )

