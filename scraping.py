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


		
