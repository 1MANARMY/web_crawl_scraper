import urllib
import re

ticker_list = []
i=0
while i < 5:
	useri = raw_input("Enter ticker: ")
	ticker_list.append(useri)
	print ticker_list
	i+=1

i=0
while i<len(ticker_list):
	url = "http://finance.yahoo.com/q?s=" +ticker_list[i] +"&ql=1"
	htmlfile = urllib.urlopen(url)
	htmltext = htmlfile.read()
	regex = '<span id="yfs_l84_'+ticker_list[i] +'">(.+?)</span>'
	pattern = re.compile(regex)
	price = re.findall(pattern,htmltext)
	print "the price of",ticker_list[i]," is " ,price
	i+=1
