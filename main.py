import requests
from urllib.parse import urlparse, urljoin
from bs4 import *
from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown
from rich.traceback import install

from crawler import crawl,crawlInt
from scraping import scraping
from mkdir import folder_create

# implementing TOR proxies
session = requests.session()
session.proxies["http"] = "socks5h://localhost:9050"
session.proxies["https"] = "socks5h://localhost:9050"

# initialize the set of links (unique links)
internal_urls = set()
external_urls = set()

# Declaring rich variables
MARK = """
# TOR CRAWLER
"""

table = Table(title="\n", style="yellow")

table.add_column("S.No", style="cyan")
table.add_column("Available Functions", style="magenta", justify="center")

table.add_row("1.", "Crawling Internal endpoints")
table.add_row("2.", "Crawling Internal and External links")
table.add_row("3.", "Scraping web pages")
table.add_row("4.", "Downloading Images")
table.add_row("5.", "Exit from the Crawler")

console = Console()

# traceback design
install()

md = Markdown(MARK)
print()
console.print(md)
console.print(table)

console.print("\nEnter an option to perform :", style="bold green")
opt = int(input())


while True:

	if opt == 1:
		console.print("\nEnter the URL :", style="bold sky_blue1")
		url=input()
		crawl(url)
		break

	elif opt == 2:
		max_urls=30
		console.print("\nEnter the URL :", style="bold sky_blue1")
		url=input()
		crawlInt(url)
		print("[+] Total Internal links:", len(internal_urls))
		print("[+] Total External links:", len(external_urls))
		print("[+] Total Crawled URLs:", len(external_urls) + len(internal_urls))
		break

	elif opt == 3:
		console.print("\nEnter the URL :", style="bold sky_blue1")
		url=input()
		scraping(url)
		break


	elif opt == 4:
		console.print("\nEnter the URL :", style="bold sky_blue1")
		url=input()
		r = session.get(url);

		# Parse HTML Code
		soup = BeautifulSoup(r.text, 'html.parser')

		# find all images in URL
		images = soup.findAll('img')

		# Call folder create function
		folder_create(images)
		break

	else:
		print("Exited")
		break
