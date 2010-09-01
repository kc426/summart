#!/usr/bin/env python
# -*- coding: utf-8 -*-

import summartUtil
import markov
import sys

DEBUG = False 

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

	if DEBUG:
		MAXGEN = 200
	else:
		MAXGEN = int(raw_input("Enter number of words you want to summarize: "))
	table = {}
	markov.build(text.split('\n'), table)
	markov.generate(table, MAXGEN)

if __name__ == "__main__":
	main()
