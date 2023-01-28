# Shadow-Spider
Darkweb crawler prototype to crawl online sites selling drugs that operates in the shadows. 

### Objective
Developed a prototype of a crawler that allows to search the sites with illegal content within the TOR network through crawlers dedicated to search, 
identify, and index secret services and black markets. Overview of the idea is to build the Architecture to 
precipitate the illegal drug selling websites on darknet. That estimates the amount of drugs, drug content and vendors from origin(India). It uses a 
combination of different technologies like scrapy to build the crawler; docker to keep the proxy server and the virtual machine with apache solr and 
MongoDB as a database. The crawler worked on the way to identify the links that are based on the pattern selling drugs.

### Source links
Hidden wiki was the only way to get the bunch of urls that are related to the illegal drug markets. In the dark web there is no sign to get the 
perfect url and it is not easy to memorize the random 56 characters ending with .onion link. So an easy way to scratch up the crawler was to start 
with links that are displayed in the hidden wiki. Once the crawler starts with the first link it will crawl through the website and find the internal 
links and external links of the website. Internal links refers to the site that are related to the same domain (ie. subdomains). External links are the
links that redirect to the other links. The crawler crawls till the fixed range set on the frontier to avoid looping in the dark web and malfunctioning. 
Scraping takes place in the final part of each url to get the details.
