# -*- coding: utf-8 -*-
import re
import urllib2


def openWebsite(link):
	response = urllib2.urlopen(link)
	html = response.read()
	latitude_finder = re.compile('(?<=class="latitude">).*?(?=<)')
	longitude_finder = re.compile('(?<=class="longitude">).*?(?=<)')

	if response.code == 200:
		latitude = latitude_finder.search(html)
		longitude = longitude_finder.search(html)
		if latitude and longitude:
			print(link.split('/')[4]+": "+latitude.group(0).decode("utf-8")+" "+longitude.group(0).decode("utf-8"))
		else:
			print("Latitude or longitude of "+link.split('/')[4]+" not found on the web")
			# exit(0)


def main():
	with open('cities.txt', 'r') as f:
		for line in f:
			openWebsite('https://en.wikipedia.org/wiki/'+line)

if __name__ == '__main__':
	main()