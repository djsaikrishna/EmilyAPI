import os
import re
import time
import urllib.parse
from base64 import b64decode, standard_b64encode

import cloudscraper
import requests
from bs4 import BeautifulSoup

BIFM_URL = os.environ.get("BIFM_URL", "https://bifm.tacohitbox.com/api/bypass?url")


def decrypt_url(code):
    a, b = "", ""
    for i in range(len(code)):
        if i % 2 == 0:
            a += code[i]
        else:
            b = code[i] + b
    key = list(a + b)
    i = 0
    while i < len(key):
        if key[i].isdigit():
            for j in range(i + 1, len(key)):
                if key[j].isdigit():
                    u = int(key[i]) ^ int(key[j])
                    if u < 10:
                        key[i] = str(u)
                    i = j
                    break
        i += 1
    key = "".join(key)
    decrypted = b64decode(key)[16:-16]
    return decrypted.decode("utf-8")


def adfly(url):
    res = requests.get(url).text
    out = {"error": False, "src_url": url}
    ysmm = re.findall("ysmm\s+=\s+['|\"](.*?)['|\"]", res)[0]
    url = decrypt_url(ysmm)
    time.sleep(10)
    if re.search(r"go\.php\?u\=", url):
        url = b64decode(re.sub(r"(.*?)u=", "", url)).decode()
    elif "&dest=" in url:
        url = urllib.parse.unquote(re.sub(r"(.*?)dest=", "", url))
    out["bypassed_url"] = url
    return out["bypassed_url"]


def adrinolinks(url):
    client = cloudscraper.create_scraper(allow_brotli=False)
    dom = "https://adrinolinks.in"
    code = url.split("/")[-1]
    f_url = f"{dom}/{code}"
    hs = {
        "referer": "https://wikitraveltips.com/",
    }
    resp = client.get(f_url, headers=hs)
    soup = BeautifulSoup(resp.content, "html.parser")
    inputs = soup.find(id="go-link").find_all(name="input")
    data = {input.get("name"): input.get("value") for input in inputs}
    h = {"x-requested-with": "XMLHttpRequest"}
    time.sleep(5)
    r = client.post(f"{dom}/links/go", data=data, headers=h)
    des_url = r.json()["url"]
    des_url = des_url.replace(" ", "%20")
    return des_url


def encod(__str: str) -> str:
    str_bytes = __str.encode("ascii")
    bytes_b64 = standard_b64encode(str_bytes)
    return bytes_b64.decode("ascii")


def bifm(url):
    url = encod(url)
    client = cloudscraper.create_scraper(allow_brotli=False)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"
    }
    apix = f"{BIFM_URL}={url}"
    time.sleep(2)
    resp = client.get(apix, headers=headers)
    query = resp.json()
    return query["destination"]


def droplink(url):
    client = cloudscraper.create_scraper(allow_brotli=False)
    res = client.get(url)
    ref = re.findall("action[ ]{0,}=[ ]{0,}['|\"](.*?)['|\"]", res.text)[0]
    h = {"referer": ref}
    res = client.get(url, headers=h)
    bs4 = BeautifulSoup(res.content, "lxml")
    inputs = bs4.find_all("input")
    data = {input.get("name"): input.get("value") for input in inputs}
    h = {
        "content-type": "application/x-www-form-urlencoded",
        "x-requested-with": "XMLHttpRequest",
    }
    p = urllib.parse.urlparse(url)
    final_url = f"{p.scheme}://{p.netloc}/links/go"
    time.sleep(4)
    res = client.post(final_url, data=data, headers=h).json()
    return res["url"]


def gplinks(url):
    client = cloudscraper.create_scraper(allow_brotli=False)
    p1 = urllib.parse.urlparse(url)
    final_url = f"{p1.scheme}://{p1.netloc}/links/go"
    res = client.head(url)
    header_loc = res.headers["location"]
    p2 = urllib.parse.urlparse(header_loc)
    ref_url = f"{p2.scheme}://{p2.netloc}/"
    h1 = {"referer": ref_url}
    res2 = client.get(url, headers=h1, allow_redirects=False)
    bs4 = BeautifulSoup(res2.content, "html.parser")
    inputs = bs4.find_all("input")
    data = {input.get("name"): input.get("value") for input in inputs}
    h2 = {
        "referer": ref_url,
        "x-requested-with": "XMLHttpRequest",
    }
    time.sleep(12)
    res3 = client.post(final_url, headers=h2, data=data)
    return res3.json()["url"].replace("\/", "/")


def gtlinks(url):
    client = requests.Session()
    url = url[:-1] if url[-1] == '/' else url
    if "theforyou.in" in url:
        token = url.split("=")[-1]
    else:
        url = requests.get(url).url
        token = url.split("=")[-1]
    domain = "https://go.kinemaster.cc/"
    response = client.get(domain+token, headers={"referer":domain+token})
    soup = BeautifulSoup(response.content, "html.parser")
    inputs = soup.find(id="go-link").find_all(name="input")
    data = { input.get('name'): input.get('value') for input in inputs }
    time.sleep(5)
    headers={"x-requested-with": "XMLHttpRequest"}
    des_url = client.post(domain+"links/go", data=data, headers=headers).json()["url"]
    des_url = des_url.replace(" ", "%20")
    return des_url


def gyanilinks(url):
    client = cloudscraper.create_scraper(allow_brotli=False)
    dom = "https://go.kinemaster.cc"
    re = client.get(url)
    f_url = re.url
    code = f_url.split("=")[-1]
    final_url = f"{dom}/{code}"
    resp = client.get(final_url)
    soup = BeautifulSoup(resp.content, "html.parser")
    inputs = soup.find(id="go-link").find_all(name="input")
    data = {input.get("name"): input.get("value") for input in inputs}
    h = {"x-requested-with": "XMLHttpRequest"}
    time.sleep(10)
    r = client.post(f"{dom}/links/go", data=data, headers=h)
    des_url = r.json()["url"]
    des_url = des_url.replace(" ", "%20")
    return des_url


def htpmovies(url):
    client = cloudscraper.create_scraper(allow_brotli=False)
    a = client.get(url, allow_redirects=True).text
    b = a.split('("')[-1]
    t_url = b.split('")')[0]
    t_url = t_url.replace("&m=1", "")
    param = t_url.split("/")[-1]
    DOMAIN = "https://go.theforyou.in"
    final_url = f"{DOMAIN}/{param}"
    resp = client.get(final_url)
    soup = BeautifulSoup(resp.content, "html.parser")    
    inputs = soup.find(id="go-link").find_all(name="input")
    data = { input.get('name'): input.get('value') for input in inputs }
    h = { "x-requested-with": "XMLHttpRequest" }
    time.sleep(10)
    r = client.post(f"{DOMAIN}/links/go", data=data, headers=h)
    return r.json()['url']


def hypershort(url):
	client = requests.Session()
	response= client.get(url)
	soup = BeautifulSoup(response.content, "html.parser")	
	token_response = client.get("https://blog.miuiflash.com/links/createToken.js").text
	token_regex = re.search("itsToken\.value = \S+", token_response)
	token = token_regex[0].split("=")[1].removesuffix('"').removeprefix(' "')
	inputs = soup.find(id="re-form").find_all(name="input")
	data = { input.get('name'): input.get('value') for input in inputs }["getData"]
	next_page_link = soup.find("form").get("action")
	resp = client.post(next_page_link, data={"itsToken":token, "get2Data":data},
	headers={"referer":next_page_link})
	soup = BeautifulSoup(resp.content, "html.parser")	
	data = { input.get('name'): input.get('value') for input in inputs }
	time.sleep(3)
	tokenize_url = soup.find(name="iframe", id="anonIt").get("src")
	tokenize_url_resp = client.get(tokenize_url)
	soup = BeautifulSoup(tokenize_url_resp.content, "html.parser")	
	time.sleep(1)
	inputs = soup.find(id="go-link").find_all(name="input")
	data = { input.get('name'): input.get('value') for input in inputs }
	final_response = client.post("https://blog.miuiflash.com/blog/links/go", data=data,cookies= tokenize_url_resp.cookies, headers={"x-requested-with": "XMLHttpRequest", "referer":tokenize_url}).json()["url"]
	return final_response


def linkvertise(url):
    client = cloudscraper.create_scraper(allow_brotli=False)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    }
    data = client.get(f"https://bypass.pm/bypass2?url={url}", headers=headers)
    query = data.json()
    if query["success"] is True:
        return query["destination"]
    else:
        data = {
            "url": url,
        }
        r = requests.post("https://api.bypass.vip/", data=data)
        time.sleep(1)
        return r.json()["destination"]


def multi_aio(url):
    data = {
        "url": url,
    }
    r = requests.post("https://api.bypass.vip/", data=data)
    time.sleep(1)
    return r.json()["destination"]


ANCHOR_URL = "https://www.google.com/recaptcha/api2/anchor?ar=1&k=6Lcr1ncUAAAAAH3cghg6cOTPGARa8adOf-y9zv2x&co=aHR0cHM6Ly9vdW8uaW86NDQz&hl=en&v=1B_yv3CBEV10KtI2HJ6eEXhJ&size=invisible&cb=4xnsug1vufyr"


def RecaptchaV3(ANCHOR_URL):
    url_base = "https://www.google.com/recaptcha/"
    post_data = "v={}&reason=q&c={}&k={}&co={}"
    client = cloudscraper.create_scraper(allow_brotli=False)
    client.headers.update({"content-type": "application/x-www-form-urlencoded"})
    matches = re.findall("([api2|enterprise]+)\/anchor\?(.*)", ANCHOR_URL)[0]
    url_base += f"{matches[0]}/"
    params = matches[1]
    res = client.get(f"{url_base}anchor", params=params)
    token = re.findall(r'"recaptcha-token" value="(.*?)"', res.text)[0]
    params = dict(pair.split("=") for pair in params.split("&"))
    post_data = post_data.format(params["v"], token, params["k"], params["co"])
    res = client.post(f"{url_base}reload", params=f'k={params["k"]}', data=post_data)
    return re.findall(r'"rresp","(.*?)"', res.text)[0]


def ouo(url):
    client = cloudscraper.create_scraper(allow_brotli=False)
    tempurl = url.replace("ouo.press", "ouo.io")
    p = urllib.parse.urlparse(tempurl)
    id = tempurl.split("/")[-1]
    res = client.get(tempurl)
    next_url = f"{p.scheme}://{p.hostname}/go/{id}"
    for _ in range(2):
        if res.headers.get("Location"):
            break
        bs4 = BeautifulSoup(res.content, "lxml")
        inputs = bs4.form.findAll("input", {"name": re.compile(r"token$")})
        data = {input.get("name"): input.get("value") for input in inputs}
        time.sleep(10)
        ans = RecaptchaV3(ANCHOR_URL)
        data["x-token"] = ans
        h = {"content-type": "application/x-www-form-urlencoded"}
        res = client.post(next_url, data=data, headers=h, allow_redirects=False)
        next_url = f"{p.scheme}://{p.hostname}/xreallcygo/{id}"
    return res.headers.get("Location")


def privatemoviez(url):
    client = cloudscraper.create_scraper(allow_brotli=False)
    r = client.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    test = soup.text
    param = test.split('console.log("')[-1]
    t_url = param.split('");')[0]
    t_url = t_url.replace("&m=1", "")     
    param = t_url.split("/")[-1]     
    DOMAIN = "https://go.kinemaster.cc"
    final_url = f"{DOMAIN}/{param}"
    resp = client.get(final_url)
    soup = BeautifulSoup(resp.content, "html.parser")    
    inputs = soup.find(id="go-link").find_all(name="input")
    data = { input.get('name'): input.get('value') for input in inputs }
    h = { "x-requested-with": "XMLHttpRequest" }
    time.sleep(10)
    r = client.post(f"{DOMAIN}/links/go", data=data, headers=h)
    return r.json()['url']


def rewayatcafe(url):
    client = cloudscraper.create_scraper(allow_brotli=False)
    p = urllib.parse.urlparse(url)
    ref = f"{p.scheme}://{p.netloc}/"
    h = {"referer": ref}
    res = client.get(url, headers=h)
    bs4 = BeautifulSoup(res.content, "html.parser")
    inputs = bs4.find_all("input")
    data = {input.get("name"): input.get("value") for input in inputs}
    h = {
        "content-type": "application/x-www-form-urlencoded",
        "x-requested-with": "XMLHttpRequest",
    }
    p = urllib.parse.urlparse(url)
    final_url = f"{p.scheme}://{p.netloc}/links/go"
    time.sleep(10)
    res = client.post(final_url, data=data, headers=h).json()
    return res["url"]


def rocklinks(url):
    client = cloudscraper.create_scraper(allow_brotli=False)
    if "rocklinks.net" in url:
        dom = "https://blog.disheye.com"
    else:
        dom = "https://rocklinks.net"
    url = url[:-1] if url[-1] == "/" else url
    code = url.split("/")[-1]
    if "rocklinks.net" in url:
        final_url = f"{dom}/{code}?quelle="
    else:
        final_url = f"{dom}/{code}"
    resp = client.get(final_url)
    soup = BeautifulSoup(resp.content, "html.parser")
    inputs = soup.find(id="go-link").find_all(name="input")
    data = {input.get("name"): input.get("value") for input in inputs}
    h = {"x-requested-with": "XMLHttpRequest"}
    time.sleep(10)
    r = client.post(f"{dom}/links/go", data=data, headers=h)
    des_url = r.json()["url"]
    des_url = des_url.replace(" ", "%20")
    return des_url


def script_b(domain, url):
    client = cloudscraper.create_scraper(allow_brotli=False)
    res = client.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    soup = soup.find("form").findAll("input")
    datalist = []
    for ele in soup:
        datalist.append(ele.get("value"))
    data = {
        "_method": datalist[0],
        "_csrfToken": datalist[1],
        "ad_form_data": datalist[2],
        "_Token[fields]": datalist[3],
        "_Token[unlocked]": datalist[4],
    }
    client.headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "en-US,en;q=0.5",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "Origin": domain,
        "Connection": "keep-alive",
        "Referer": url,
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
    }
    time.sleep(12)
    response = client.post(domain + "/links/go", data=data).json()
    furl = response["url"]
    return furl


def script_a(url):
    client = cloudscraper.create_scraper(allow_brotli=False)
    res = client.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    soup = soup.find("form")
    action = soup.get("action")
    soup = soup.findAll("input")
    rurl = ""
    datalist = []
    for ele in soup:
        datalist.append(ele.get("value"))
    client.headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Origin": action,
        "Connection": "keep-alive",
        "Referer": action,
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
    }
    data = {
        "newwpsafelink": datalist[1],
        "g-recaptcha-response": RecaptchaV3(ANCHOR_URL),
    }
    response = client.post(action, data=data)
    soup = BeautifulSoup(response.text, "html.parser")
    soup = soup.findAll("div", class_="wpsafe-bottom text-center")
    for ele in soup:
        rurl = ele.find("a").get("onclick")[13:-12]
    res = client.get(rurl)
    furl = res.url
    script_dom = f"https://{furl.split('/')[-2]}/"
    return script_b(script_dom, furl)


def shareus(url):
    client = cloudscraper.create_scraper(allow_brotli=False)
    token = url.split("=")[-1]
    des_url = f"https://us-central1-my-apps-server.cloudfunctions.net/r?shortid={token}"
    dest_url = client.get(des_url).text
    return dest_url


def shorte(url):
    client = cloudscraper.create_scraper(allow_brotli=False)
    client.headers.update({"referer": url})
    p = urllib.parse.urlparse(url)
    res = client.get(url)
    sess_id = re.findall("""sessionId(?:\s+)?:(?:\s+)?['|"](.*?)['|"]""", res.text)[0]
    final_url = f"{p.scheme}://{p.netloc}/shortest-url/end-adsession"
    params = {"adSessionId": sess_id, "callback": "_"}
    time.sleep(5)
    res = client.get(final_url, params=params)
    dest_url = re.findall('"(.*?)"', res.text)[1].replace("\/", "/")
    dest_url = dest_url.replace(" ", "%20")
    return dest_url


def shortingly(url):
    client = cloudscraper.create_scraper(allow_brotli=False)
    dom = "https://go.techyjeeshan.xyz"
    url = url[:-1] if url[-1] == "/" else url
    code = url.split("/")[-1]
    final_url = f"{dom}/{code}"
    resp = client.get(final_url)
    soup = BeautifulSoup(resp.content, "html.parser")
    inputs = soup.find(id="go-link").find_all(name="input")
    data = {input.get("name"): input.get("value") for input in inputs}
    h = {"x-requested-with": "XMLHttpRequest"}
    time.sleep(10)
    r = client.post(f"{dom}/links/go", data=data, headers=h)
    des_url = r.json()["url"]
    des_url = des_url.replace(" ", "%20")
    return des_url


def sirigan(url):
    client = cloudscraper.create_scraper(allow_brotli=False)
    time.sleep(3)
    res = client.get(url)
    url = res.url.split("=", maxsplit=1)[-1]
    while True:
        try:
            url = b64decode(url).decode("utf-8")
        except BaseException:
            break
    return url.split("url=")[-1]


def tnlink(url):
    url = url[:-1] if url[-1] == "/" else url
    token = url.split("/")[-1]
    client = cloudscraper.create_scraper(allow_brotli=False)
    h1 = {
        "referer": "https://usanewstoday.club/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    }
    resp = client.get(f"https://gadgets.usanewstoday.club/{token}", headers=h1)
    soup = BeautifulSoup(resp.content, "html.parser")
    inputs = soup.find(id="go-link").find_all(name="input")
    data = {input.get("name"): input.get("value") for input in inputs}

    time.sleep(8)
    h2 = {
        "x-requested-with": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    }
    dest_url = client.post(
        "https://gadgets.usanewstoday.club/links/go", data=data, headers=h2
    ).json()["url"]
    return dest_url


def xpshort(url):
    client = requests.Session()
    dom = "https://push.bdnewsx.com"
    url = url[:-1] if url[-1] == "/" else url
    code = url.split("/")[-1]
    final_url = f"{dom}/{code}"
    r = client.get(url)
    ref = re.findall("action[ ]{0,}=[ ]{0,}['|\"](.*?)['|\"]", r.text)[0]
    h = {"referer": ref}
    resp = client.get(final_url, headers=h)
    soup = BeautifulSoup(resp.content, "html.parser")
    inputs = soup.find(id="go-link").find_all(name="input")
    data = {input.get("name"): input.get("value") for input in inputs}
    h = {"x-requested-with": "XMLHttpRequest"}
    time.sleep(8)
    r = client.post(f"{dom}/links/go", data=data, headers=h)
    return r.json()["url"]
