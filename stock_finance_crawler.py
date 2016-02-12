#!/usr/bin/python

import urllib
import re
import tempfile
#starts itself once initiated
if __name__ == "__main__":
#creates tmp file to balance the data flow
	t = tempfile.NamedTemporaryFile(mode="r+")
	with open("ticker_input.txt", "rb+") as f:
#will open the ticker file as f this is our data to enter into crawler
		ticker_list	 = f.read().splitlines()
		i=0
		while i<len(ticker_list):
			try:
#we begin with trying the tickers into the google finance url one by one
#this url goes straight to the xml data making it the fastest option without an API
				htmltext = urllib.urlopen("https://www.google.com/finance/getprices?q=" +ticker_list[i] +"&x=NASD&i=120&p=25m&f=c").read()
				price = htmltext.split()[len(htmltext.split())-1]
# the contents from the urlopen will be sliced and diced to give us the last piece of data 
				if price != "DATA=":
#checks to see if the final piece of data doesnt = DATA=
#if it isn't data= then it has a price
					output = "Ticker: " + ticker_list[i] + " = " + price
					t.write(output +"\n")
				else:
#if it the price data comes back data= then the ticker entered wasn't in the NASDAQ
					output = "Ticker: " + ticker_list[i] + " = " + "Not Part of the NASDQ"
					t.write(output +"\n")
				i+=1
			except:
				f.write("Error: Your List Is Empty.")
#A little error handling for empty spaces in file or if you configure this to get inputs
		f.close()
		t.seek(0)
		o = open("ticker_input.txt", "w+")
		for line in t:
#then wrap it up with the new contents line per line
			o.write(line)
		t.close()