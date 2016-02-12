#!/usr/bin/python

import os
import time

file_check = os.stat("ticker_input.txt").st_mtime
#checks to see if the files time from last alteration was changed
def fileChecker():
	while (os.stat("ticker_input.txt").st_mtime == file_check):
#if it is equal to itself we pass giving it a contat loop till broken
		pass
	else:
#if the file doesn't equal itself then execute out webcrawler 
		execfile("pyweb_scraper.py")
if __name__ == "__main__":
	fileChecker()