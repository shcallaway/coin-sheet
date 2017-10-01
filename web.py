import re, httplib2
from lxml import html

def scrape(url):
  http = httplib2.Http()
  (headers, content) = http.request(url, 'GET')
  return html.fromstring(content)

def get_page_text(page, xpath):
  text = page.xpath(xpath)

  # handle list return type
  if isinstance(text, list):
    text = text[0]

  return text.strip()

# to scrape, if necessary:

# from selectors import coinmarketcap

# page = scrape('https://coinmarketcap.com/')
# btc_cap = get_page_text(page, coinmarketcap['btc']['market_cap'])
# eth_cap = get_page_text(page, coinmarketcap['eth']['market_cap'])
