import bs4, requests

def getAmazonPrice(productUrl):
	res = requests.get(productUrl)
	res.raise_for_status()

	soup = bs4.BeautifulSoup(res.text, 'html.parser')
	elems = soup.select('#Copy SELECTOR FROM INSPECT ELEMENT / OR COPY CSS PATH')
	return elems[0].text.strip()

price = getAmazonPrice('url')
print('The price is ' + price)
