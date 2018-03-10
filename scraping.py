from bs4 import BeautifulSoup
import requests

def scrape():
	data = []
	url_main = "http://eltiempo.com"

	r = requests.get(url_main)
	soup = BeautifulSoup(r.text, "html.parser")
	articles = soup.find_all("h3", class_="listing-title")

	for article in articles:
		info = {}
		link = article.find("a")
		#title
		info["title"] = link.text

		#url
		info["url"] = url_main + link['href']
		
		data.append(info)

	return data

def scrapeWord():
	url_main = "http://spanishdict.com/wordoftheday"
	
	r = requests.get(url_main)
	soup = BeautifulSoup(r.text, "html.parser")

	container = soup.find("div", class_="sd-wotd-container")
	data = {}

	data["word"] = container.find("a", class_="sd-wotd-headword-link").text
	data["translation"] = container.find("div", class_="sd-wotd-translation").text
	data["example"] = container.find("div", class_="sd-wotd-example-source").text


	#data["word"] = "towel"
	#data["translation"] = "toalla"
	#data["example"] = "Tu eres una toalla"

	return data


