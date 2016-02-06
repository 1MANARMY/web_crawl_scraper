import urllib
import re

ticker_list = []
def ticker_entry():
	i=0
	while i < 5:
		useri = raw_input("Enter ticker: ")
		ticker_list.append(useri)
		i+=1
		yahoo_scrape()

def yahoo_scrape():
	i=0
	while i<len(ticker_list):
		url = "http://finance.yahoo.com/q?s=" +ticker_list[i]
		htmlfile = urllib.urlopen(url)
		htmltext = htmlfile.read()
		regex = '<span id="yfs_l84_'+ticker_list[i] +'">(.+?)</span>'
		pattern = re.compile(regex)
		price = re.findall(pattern,htmltext)
		return "the price of"+ticker_list[i]+" is " + price[0]
		i+=1

def google_net_scrape(ticker_list):
	i=0
	while i<len(ticker_list):
		htmltext = urllib.urlopen("https://www.google.com/finance/getprices?q=" +ticker_list[i] +"&x=NASD&i=120&p=25m&f=c")
		return "the price of" + ticker_list[i] + " is " + htmltext.split()[len(htmltext.split())-1]
		i+=1
if __name__ == "__main__":
	ticker_entry()
