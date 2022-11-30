import re
import requests

from web import LOGGER
from web.scripts.telegraph_helper import telegraph, telegraph_name


async def telegraph_paste(text):
    tele_cont = []
    path = []
    if len(text.encode("utf-8")) > 39000:
        tele_cont.append(text)
    if text != "":
        tele_cont.append(text)
    if len(tele_cont) == 0:
        return "", None
    for content in tele_cont:
        path.append(
            telegraph.create_page(title=telegraph_name, content=content)["path"]
        )
    if len(path) > 1:
        telegraph.edit_telegraph(path, tele_cont)
    tlg_url = f"https://graph.org/{path[0]}"
    return tlg_url


async def katbin_paste(text):
    global token
    base_url = "https://katb.in/"
    client = requests.Session()
    ptn = r'name="_csrf_token".+value="(.+)"'
    resp = client.get(base_url)
    for i in re.finditer(ptn, resp.text):
        token = i.group(1)
        break
    data = {"_csrf_token": token, "paste[content]": text}
    pst_url = client.post(base_url, data=data).url
    return pst_url


async def nekobin_paste(text):
    base_url = "https://nekobin.com/"
    client = requests.Session()
    data = {"content": text}
    res = client.post(base_url + "api/documents", json=data).json()
    pst_url = base_url + res["result"]["key"]
    return pst_url


async def hastebin_paste(text):
    base_url = "https://hastebin.com/"
    client = requests.Session()
    res = client.post(base_url + "documents", json=text).json()
    pst_url = base_url + res["key"]
    return pst_url


async def rentry_paste(text):
    global token
    base_url = "https://rentry.co/"
    client = requests.Session()
    ptn = r'name="csrfmiddlewaretoken" value="(.+)"'
    resp = client.get(base_url)
    for i in re.finditer(ptn, resp.text):
        token = i.group(1)
        break
    data = dict(csrfmiddlewaretoken=token, text=text)
    headers=dict(Referer=base_url)
    pst_url = client.post(base_url, data=data, headers=headers).url
    return pst_url


async def pastingga_paste(text):
    base_url = "https://pasting.ga/"
    client = requests.Session()
    data = {"heading": telegraph_name, "content": text}
    res = client.post(base_url + "api", json=data).json()
    pst_url = base_url + res["key"]
    return pst_url


async def pastylus_paste(text):
    global code
    try:
        base_url = "https://pasty.lus.pm/"
        client = requests.Session()
        data = {"content": text}
        res = client.post(base_url + "api/v2/pastes/", json=data)
        for i in re.finditer(r'"id":\s?"(.+?)"', res.text):
            code = i.group(1)
            break
        pst_url = base_url + code
        return pst_url
    except Exception as e:
        LOGGER.error(f"Error while pasting to PastyLus: {e}")
        return f"Error while pasting to PastyLus: {e}"


async def spacebin_paste(text):
    global code
    base_url = "https://spaceb.in/"
    client = requests.Session()
    data = dict(content=text, extension="markdown")
    res = client.post(base_url + "api/v1/documents/", data=data)
    for i in re.finditer(r'"id":\s?"(.+?)"', res.text):
        code = i.group(1)
        break
    pst_url = base_url + code
    return pst_url
