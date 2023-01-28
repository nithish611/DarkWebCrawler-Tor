from bs4 import *
import requests

# implementing TOR proxies
session = requests.session()
session.proxies["http"] = "socks5h://localhost:9050"
session.proxies["https"] = "socks5h://localhost:9050"

def scraping(url):

	response = session.get(url)
	
	soup = BeautifulSoup(response.content, "html.parser")

	# Extract title of page
	page_title = soup.title.text

	# Extract body of page
	page_body = soup.body

	# Extract head of page
	page_head = soup.head

	# print the result
	print(page_body)
