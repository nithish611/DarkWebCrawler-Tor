import requests
from bs4 import *
from urllib.parse import urlparse, urljoin
from colorify import GREEN,GRAY,RESET,YELLOW,CYAN,BLUE

# implementing TOR proxies
session = requests.session()
session.proxies["http"] = "socks5h://localhost:9050"
session.proxies["https"] = "socks5h://localhost:9050"

# initialize the set of links (unique links)
internal_urls = set()
external_urls = set()

def crawl(url):

    response = session.get(url)
    urls = set()

    soup = BeautifulSoup(response.content, "html.parser")

    # title of the webpage
    print(f"{CYAN}\n[*] PAGE TITLE : ", soup.title.string)

    # get all the links on the webpage
    print(f"{YELLOW}\n[*] CRAWLED LINKS : \n")
    for link in soup.find_all("a"):
        # Need to change the content to crawl startswith. can include class name and xpath
        if link.get("href").startswith("/"):
            print(url + link.get("href"))
            urls.add(link)
        else:
            print(link.get("href"))
            urls.add(link)

    # extract text from the webpage
    # print(soup.get_text())

    print(f"{BLUE}\n[+] Total Crawled links:", len(urls))


def is_valid(url):
    """
    Checks whether `url` is a valid URL.
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def get_all_website_links(url):
    """
    Returns all URLs that is found on `url` in which it belongs to the same website
    """
    urls = set()
    response = session.get(url)
    # domain name of the URL without the protocol
    domain_name = urlparse(url).netloc
    soup = BeautifulSoup(response.content, "html.parser")

    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None:
            # href empty tag
            continue
        
        # join the URL if it's relative (not absolute link)
        href = urljoin(url, href)

        parsed_href = urlparse(href)
        # remove URL GET parameters, URL fragments, etc.
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path

        if not is_valid(href):
            # not a valid URL
            continue
        if href in internal_urls:
            # already in the set
            continue
        if domain_name not in href:
            # external link
            if href not in external_urls:
                print(f"{GRAY}[!] External link: {href}{RESET}")
                external_urls.add(href)
            continue
        print(f"{GREEN}[*] Internal link: {href}{RESET}")
        urls.add(href)
        internal_urls.add(href)
    return urls

# number of urls visited so far will be stored here
total_urls_visited = 0

def crawlInt(url, max_urls=30):
    """
    Crawls a web page and extracts all links.
    You'll find all links in `external_urls` and `internal_urls` global set variables.
    params:
        max_urls (int): number of max urls to crawl, default is 30.
    """
    global total_urls_visited
    total_urls_visited += 1
    print(f"{YELLOW}[*] Crawling: {url}{RESET}")
    links = get_all_website_links(url)
    for link in links:
        if total_urls_visited > max_urls:
            break
        crawlInt(link, max_urls=max_urls)

