#!/usr/bin/env python
# -*- coding: utf-8 -*-

import summartUtil
import markov

DEBUG = True

def main():
	if DEBUG:
		url = "http://www.cs.drexel.edu/~jpopyack/Kasparov.html"
		MAXGEN = 200
	else:
		url = raw_input("Enter the URL: ")
		MAXGEN = int(raw_input("Enter number of words you want to summarize: "))
	text = summartUtil.getHtmlText(url)
	table = {}
	markov.build(text.split('\n'), table)
	markov.generate(table, MAXGEN)

if __name__ == "__main__":
	main()
