import urllib
import re

htmltext = urllib.urlopen("https://www.google.com/finance/getprices?q=AAPL&x=NASD&i=120&p=25m&f=c").read()
print htmltext.split()[len(htmltext.split())-1]
