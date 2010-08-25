#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import urllib

def main():
	word = raw_input("input the word:")
	print getWordFunction(word)

def getWordFunction(word):
	f = urllib.urlopen("http://www2.merriam-webster.com/cgi-bin/collegiate?"+word)
	s = f.read()
	f.close()
	text = html2txt(s)
	for line in text.split('\n'):
		if line.startswith("Function:"):
			field = line.split(':')
			return field[1].strip()

def html2txt(s, hint = 'entity', code = 'ISO-8859-1'):
	"""Convert the html to raw txt
	- suppress all return
	- <p>, <tr>, <br> to return
	- <td> to tab
	Need the foolwing regex:
	p = re.compile('(<p.*?>)|(<tr.*?>)', re.I)
	t = re.compile('<td.*?>', re.I)
	comm = re.compile('<!--.*?-->', re.M)
	tags = re.compile('<.*?>', re.M)
	version 0.0.1 20020930
	"""
	p = re.compile('(<p.*?>)|(<tr.*?>)|<br.*?>', re.I)
	t = re.compile('<td.*?>', re.I)
	comm = re.compile('<!--.*?-->', re.M)
	tags = re.compile('<.*?>', re.M)

	s = s.replace('\n', '') # remove returns time this compare to split filter join
	s = p.sub('\n', s) # replace p and tr by \n
	s = t.sub('\t', s) # replace td by \t
	s = comm.sub('', s) # remove comments
	s = tags.sub('', s) # remove all remaining tags
	s = re.sub(' +', ' ', s) # remove running spaces this remove the \n and \t
	# handling of entities
	result = s
	pass
	return result

if __name__ == "__main__":
	main()

