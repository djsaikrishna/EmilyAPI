import os

import requests

SAFONE_API_URL = os.environ.get("SAFONE_API_URL", "https://api.safone.tech/")


def wiki_search(query):
    api_url = f"{SAFONE_API_URL}wiki"
    resp = requests.get(api_url, params={"query": query})
    search_res = resp.text.strip()
    return search_res


def xda_search(query):
    api_url = f"{SAFONE_API_URL}xda"
    resp = requests.get(api_url, params={"query": query})
    search_res = resp.text.strip()
    return search_res


def youtube_search(query):
    api_url = f"{SAFONE_API_URL}youtube"
    resp = requests.get(api_url, params={"query": query})
    search_res = resp.text.strip()
    return search_res


def dictionary_search(query):
    api_url = f"{SAFONE_API_URL}dictionary"
    resp = requests.get(api_url, params={"query": query})
    search_res = resp.text.strip()
    return search_res


def google_search(query):
    api_url = f"{SAFONE_API_URL}google"
    resp = requests.get(api_url, params={"query": query})
    search_res = resp.text.strip()
    return search_res


def github_search(query):
    api_url = f"{SAFONE_API_URL}github"
    resp = requests.get(api_url, params={"query": query})
    search_res = resp.text.strip()
    return search_res


def image_search(query):
    api_url = f"{SAFONE_API_URL}image"
    resp = requests.get(api_url, params={"query": query})
    search_res = resp.text.strip()
    return search_res


def lyrics_search(query):
    api_url = f"{SAFONE_API_URL}lyrics"
    resp = requests.get(api_url, params={"query": query})
    search_res = resp.text.strip()
    return search_res


def npm_search(query):
    api_url = f"{SAFONE_API_URL}npm"
    resp = requests.get(api_url, params={"query": query})
    search_res = resp.text.strip()
    return search_res


def pypi_search(query):
    api_url = f"{SAFONE_API_URL}pypi"
    resp = requests.get(api_url, params={"query": query})
    search_res = resp.text.strip()
    return search_res


def reddit_search(query):
    api_url = f"{SAFONE_API_URL}reddit"
    resp = requests.get(api_url, params={"query": query})
    search_res = resp.text.strip()
    return search_res


def spellcheck(query):
    api_url = f"{SAFONE_API_URL}spellcheck"
    resp = requests.get(api_url, params={"text": query})
    search_res = resp.text.strip()
    return search_res


def tgsticker_search(query):
    api_url = f"{SAFONE_API_URL}tgsticker"
    resp = requests.get(api_url, params={"query": query})
    search_res = resp.text.strip()
    return search_res


def stackoverflow_search(query):
    api_url = f"{SAFONE_API_URL}stackoverflow"
    resp = requests.get(api_url, params={"query": query})
    search_res = resp.text.strip()
    return search_res


def torrent_search(query):
    api_url = f"{SAFONE_API_URL}torrent"
    resp = requests.get(api_url, params={"query": query})
    search_res = resp.text.strip()
    return search_res


def tmdb_search(query):
    api_url = f"{SAFONE_API_URL}tmdb"
    resp = requests.get(api_url, params={"query": query})
    search_res = resp.text.strip()
    return search_res


def urban_search(query):
    api_url = f"{SAFONE_API_URL}urban"
    resp = requests.get(api_url, params={"query": query})
    search_res = resp.text.strip()
    return search_res


def unsplash_search(query):
    api_url = f"{SAFONE_API_URL}unsplash"
    resp = requests.get(api_url, params={"query": query})
    search_res = resp.text.strip()
    return search_res
