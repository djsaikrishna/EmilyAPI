import os
import re

import jikanpy
import requests
import wikipedia
from bs4 import BeautifulSoup
from textblob import TextBlob

SAFONE_API_URL = os.environ.get("SAFONE_API_URL", "https://api.safone.tech/")


async def wiki_search(query):
    search_res = wikipedia.summary(query)
    return search_res


async def xda_search(query):
    srch_url = "https://www.xda-developers.com/search/" + query.replace(" ", "+")
    ct = requests.get(srch_url)
    search_res = ""
    ml = BeautifulSoup(ct.content, "html.parser", from_encoding="utf-8")
    ml = ml.find_all("div", re.compile("layout_post_"), id=re.compile("post-"))
    for on in ml:
        data = on.find_all("img", "xda_image")[0]
        title = data["alt"]
        thumb = data["src"]
        hre = on.find_all("div", "item_content")[0].find("h4").find("a")["href"]
        desc = on.find_all("div", "item_meta clearfix")[0].text
        text = f"[{title}]({hre})"
        search_res += (
            f"Title:{title}\nDescription:{desc}\nURL:{hre}\nThumbnail:{thumb}\n{text}"
        )
    return search_res


async def youtube_search(query):
    api_url = f"{SAFONE_API_URL}youtube"
    resp = requests.get(api_url, params={"query": query})
    search_res = resp.text.strip()
    return search_res


async def dictionary_search(query):
    api_url = f"{SAFONE_API_URL}dictionary"
    resp = requests.get(api_url, params={"query": query})
    search_res = resp.text.strip()
    return search_res


async def google_search(query):
    api_url = f"{SAFONE_API_URL}google"
    resp = requests.get(api_url, params={"query": query})
    search_res = resp.text.strip()
    return search_res


async def github_search(query):
    api_url = f"{SAFONE_API_URL}github"
    resp = requests.get(api_url, params={"query": query})
    search_res = resp.text.strip()
    return search_res


async def image_search(query):
    api_url = f"{SAFONE_API_URL}image"
    resp = requests.get(api_url, params={"query": query})
    search_res = resp.text.strip()
    return search_res


async def lyrics_search(query):
    api_url = f"{SAFONE_API_URL}lyrics"
    resp = requests.get(api_url, params={"query": query})
    search_res = resp.text.strip()
    return search_res


async def npm_search(query):
    srch_url = (
        f"https://registry.npmjs.com/-/v1/search?text={query.replace(' ','+')}&size=7"
    )
    data = requests.get(srch_url)
    search_res = ""
    for obj in data["objects"]:
        package = obj["package"]
        url = package["links"]["npm"]
        title = package["name"]
        keys = package.get("keywords", [])
        text = f"**[{title}]({package['links'].get('homepage', '')})\n{package['description']}**\n"
        text2 = f"**Version:** `{package['version']}`\n"
        text3 = f"**Keywords:** `{','.join(keys)}`"
        search_res += (
            f"Title:{title}\nURL:{url}\nKeywords:{keys}\n\n{text}{text2}{text3}"
        )
    return search_res


async def pypi_search(query):
    api_url = f"{SAFONE_API_URL}pypi"
    resp = requests.get(api_url, params={"query": query})
    search_res = resp.text.strip()
    return search_res


async def reddit_search(query):
    api_url = f"{SAFONE_API_URL}reddit"
    resp = requests.get(api_url, params={"query": query})
    search_res = resp.text.strip()
    return search_res


async def spellcheck(query):
    res = TextBlob(query)
    search_res = res.correct()
    return search_res


async def tgsticker_search(query):
    api_url = f"{SAFONE_API_URL}tgsticker"
    resp = requests.get(api_url, params={"query": query})
    search_res = resp.text.strip()
    return search_res


async def stackoverflow_search(query):
    api_url = f"{SAFONE_API_URL}stackoverflow"
    resp = requests.get(api_url, params={"query": query})
    search_res = resp.text.strip()
    return search_res


async def torrent_search(query):
    api_url = f"{SAFONE_API_URL}torrent"
    resp = requests.get(api_url, params={"query": query})
    search_res = resp.text.strip()
    return search_res


async def tmdb_search(query):
    api_url = f"{SAFONE_API_URL}tmdb"
    resp = requests.get(api_url, params={"query": query})
    search_res = resp.text.strip()
    return search_res


async def urban_search(query):
    api_url = f"{SAFONE_API_URL}urban"
    resp = requests.get(api_url, params={"query": query})
    search_res = resp.text.strip()
    return search_res


async def unsplash_search(query):
    api_url = f"{SAFONE_API_URL}unsplash"
    resp = requests.get(api_url, params={"query": query})
    search_res = resp.text.strip()
    return search_res


async def koo_search(query):
    search_res = ""
    se_ = None
    key_count = None
    query = query.replace(" ", "+")
    srch_url = f"https://www.kooapp.com/apiV1/search?query={query}&searchType=EXPLORE"
    req = requests.get(srch_url).json()
    if key_count:
        try:
            se_ = [req["feed"][key_count - 1]]
        except KeyError:
            pass
    if not se_:
        se_ = req["feed"]
    for count, feed in enumerate(se_[:10]):
        if feed["uiItemType"] == "search_profile":
            count += 1
            item = feed["items"][0]
            profileImage = (
                item["profileImageBaseUrl"]
                if item.get("profileImageBaseUrl")
                else "https://telegra.ph/file/dc28e69bd7ea2c0f25329.jpg"
            )
            temp_url = "https://www.kooapp.com/apiV1/users/handle/" + item["userHandle"]
            extra = requests.get(temp_url).json()
            text = f"‣ **Name :** `{item['name']}`"
            if extra.get("title"):
                text += f"\n‣ **Title :** `{extra['title']}`"
            text += f"\n‣ **Username :** `@{item['userHandle']}`"
            if extra.get("description"):
                text += f"\n‣ **Description :** `{extra['description']}`"
            text += f"\n‣ **Followers :** `{extra['followerCount']}`    ‣ **Following :** {extra['followingCount']}"
            if extra.get("socialProfile") and extra["socialProfile"].get("website"):
                text += f"\n‣ **Website :** {extra['socialProfile']['website']}"
            desc = item.get("title") or f"@{item['userHandle']}"
            search_res += f"Title:{item['name']}\nDescription:{desc}\nProfile Image:{profileImage}\n{text}"
    return search_res


async def animechar_search(query):
    jikan = jikanpy.jikan.Jikan()
    try:
        s = jikan.search("character", query)
    except jikanpy.exceptions.APIException:
        return "`Couldn't find character!`"
    a = s["results"][0]["mal_id"]
    char_json = jikan.character(a)
    pic = char_json["image_url"]
    msg = f"**[{char_json['name']}]({char_json['url']})\nImage:{pic}**"
    if char_json["name_kanji"] != "Japanese":
        msg += f" [{char_json['name_kanji']}]\n"
    else:
        msg += "\n"
    if char_json["nicknames"]:
        nicknames_string = ", ".join(char_json["nicknames"])
        msg += f"\n**Nicknames** : `{nicknames_string}`\n"
    about = char_json["about"].split("\n", 1)[0].strip().replace("\n", "")
    msg += f"\n**About**: __{about}__"
    return msg


async def winget_search(query):
    search_res = ""
    query = query.replace(" ", "+")
    srch_url = f"https://api.winget.run/v2/packages?ensureContains=true&partialMatch=true&take=20&query={query}"
    req = requests.get(srch_url).json()
    for on in req["Packages"]:
        data = on["Latest"]
        name = data["Name"]
        homep = data.get("Homepage")
        text = f"> **{name}**\n - {data['Description']}\n\n`winget install {on['Id']}`\n\n**Version:** `{on['Versions'][0]}`\n"
        text += "**Tags:**" + " ".join([f"#{_}" for _ in data["Tags"]])
        if homep:
            text += f"\n\n{homep}"
        search_res += f"URL:{homep}\n{text}"
    return search_res


async def omgubuntu_search(query):
    search_res = ""
    get_web = "https://www.omgubuntu.co.uk/?s=" + query.replace(" ", "+")
    get_ = requests.get(get_web).content
    BSC = BeautifulSoup(get_, "html.parser", from_encoding="utf-8")
    for cont in BSC.find_all("div", "sbs-layout__item"):
        img = cont.find("div", "sbs-layout__image")
        url = img.find("a")["href"]
        src = img.find("img")["src"]
        con = cont.find("div", "sbs-layout__content")
        tit = con.find("a", "layout__title-link")
        title = tit.text.strip()
        desc = con.find("p", "layout__description").text.strip()
        text = f"[{title.strip()}]({url})\n\n{desc}"
        search_res += (
            f"Title:{title}\nImage:{src}\nDescription:{desc}\nURL:{url}\n{text}"
        )
    return search_res
