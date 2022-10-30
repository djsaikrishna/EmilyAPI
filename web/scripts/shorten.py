import requests
from BitlyAPI import shorten_urls as bitly_short

from web.scripts.parser import OHTMLParser


def bitly_shorten(url):
    url_dict = [url]
    short_url = bitly_short(url_dict)
    for i in short_url:
        return i.short_url


def dagd_shorten(url):
    api_url = "https://da.gd/shorten"
    resp = requests.get(api_url, params={"url": url})
    short_url = resp.text.strip()
    return short_url


def tinyurl_shorten(url):
    api_url = "https://tinyurl.com/api-create.php"
    resp = requests.get(api_url, params={"url": url})
    short_url = resp.text.strip()
    return short_url


def osdb_shorten(url):
    api_url = "http://osdb.link/"
    resp = requests.post(api_url, data={"url": url})
    p = OHTMLParser()
    p.feed(resp.text)
    short_url = p.val
    return short_url


def ttm_shorten(url):
    api_url = "https://ttm.sh"
    resp = requests.post(api_url, data={"shorten": url})
    short_url = resp.text
    return short_url


def isgd_shorten(url):
    api_url = "http://is.gd/create.php"
    params = {"format": "simple", "url": url}
    resp = requests.post(api_url, params=params)
    short_url = resp.text.strip()
    return short_url


def vgd_shorten(url):
    api_url = "http://v.gd/create.php"
    params = {"format": "simple", "url": url}
    resp = requests.post(api_url, params=params)
    short_url = resp.text.strip()
    return short_url


def clckru_shorten(url):
    api_url = "https://clck.ru/--"
    resp = requests.get(api_url, params={"url": url})
    short_url = resp.text.strip()
    return short_url


def clilp_shorten(url):
    api_url = "http://chilp.it/api.php"
    resp = requests.get(api_url, params={"url": url})
    short_url = resp.text.strip()
    return short_url
