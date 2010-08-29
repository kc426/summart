#!/usr/bin/python
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

MAXGEN = 10000;	# max # of words to output
NONWORD = "\n";	# sentinel

MAX_LINE_LEN = 76	# for output only
	# note, a single string > 76 chars will not be broken



########   BUILD TABLE   #############

def build( istream, table ) :
	"""Given an istream file and a hash table, reads istream, placing
	prefix/suffix pairs into the dictionary
	Returns the # of words inserted into table"""

	w1 = w2 = NONWORD	# initial state
	rV = 0

	for l in istream :			# grab a line
		l = l.strip()
		for tok in l.split() :		# grab each word (with pumctuation and caps)
			rV += 1
			key = (w1,w2)
				# insert state into table
			if table.has_key( key ) :		# just append to satellite data
				table[ key ].append( tok )
			else :											# new entry.  create list
				table[ key ] = [ tok ]

				# move our prefix ahead
			w1, w2 = w2, tok

		# EOF, so, close the story (insert "stop here" marker into table)
	key = (w1, w2)
	if table.has_key( key ) :
		table[ key ].append( NONWORD )
	else :
		table[ key ] = [ NONWORD ]
	
	return rV


######   GENERATE TEXT   ####################

def generate( table ) :
	"""Given a table (a Markov Chain), starts at (NONWORD,NONWORD), prints a
		single story
	Returns: # of words output"""

		# set our "start" condition
	w1 = w2 = NONWORD;

	line = ""	# to accumulate words, print a line at a time

	for i in range( MAXGEN ) :
			# get our hands on the list
		key = (w1,w2)
		sufList = table[key]
			# choose a suffix from the list
		suf = random.choice( sufList )

		if suf == NONWORD :	# caught our "end story" marker.  Get out
			if len( line ) > 0 :
				print line
			break
		if len( line ) + len( suf ) > MAX_LINE_LEN :
			print line
			line = ""
		line = line + " " + suf

		w1, w2 = w2, suf

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
	
	generate( table )


# check to see if we are being called explicitly, or imported
if __name__ == "__main__" :
	sys.exit( main() )

