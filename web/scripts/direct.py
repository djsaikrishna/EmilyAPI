import json
import re
import time
import urllib.parse

import cloudscraper
import requests
from bs4 import BeautifulSoup
from lk21 import Bypass

from web.scripts.pasting import telegraph_paste


def androiddatahost(url):
    link = re.findall(r"\bhttps?://androiddatahost\.com\S+", url)[0]
    url3 = BeautifulSoup(requests.get(link).content, "html.parser")
    fin = url3.find("div", {"download2"})
    dl_url = fin.find("a")["href"]
    dl_url = dl_url.replace(" ", "%20")
    return dl_url


def bunkr_cyber(url):
    count = 1
    dl_msg = ""
    resp = requests.get(url)
    link_type = "Bunkr" if "bunkr.is" in url else "CyberDrop"
    soup = BeautifulSoup(resp.content, "html.parser")
    if link_type == "Bunkr":
        if "stream.bunkr.is" in url:
            durl = url.replace("stream.bunkr.is/v", "media-files9.bunkr.is")
            return durl
        json_data_element = soup.find("script", {"id": "__NEXT_DATA__"})
        json_data = json.loads(json_data_element.string)
        files = json_data["props"]["pageProps"]["files"]
        for file in files:
            item_url = "https://media-files.bunkr.is/" + file["name"]
            item_url = item_url.replace(" ", "%20")
            dl_msg += f"<b>{count}.</b> <code>{item_url}</code><br>"
            count += 1
    else:
        items = soup.find_all("a", {"class": "image"})
        for item in items:
            item_url = item["href"]
            item_url = item_url.replace(" ", "%20")
            dl_msg += f"<b>{count}.</b> <code>{item_url}</code><br>"
            count += 1
    fld_msg = f"<b><i>Your provided {link_type} link is of Folder and I've Found {count - 1} files in the Folder.</i></b><br>"
    fld_msg += f"<i>I've generated Direct Links for all the files.</i><br><br>"
    tlg_url = telegraph_paste(fld_msg + dl_msg)
    return tlg_url


def anonfiles(url):
    return Bypass().bypass_anonfiles(url)


def antfiles(url):
    return Bypass().bypass_antfiles(url)


def artstation(url):
    url = url.split("/")[-1]
    client = cloudscraper.create_scraper(interpreter="nodejs", allow_brotli=False)
    h = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36"
    }
    apix = f"https://www.artstation.com/projects/{url}.json"
    time.sleep(2)
    resp = client.get(apix, headers=h)
    uhh = resp.json()
    dl_url = uhh["assets"][0]["image_url"]
    return dl_url


def fembed(url):
    dl_url = Bypass().bypass_fembed(url)
    count = len(dl_url)
    lst_link = [dl_url[i] for i in dl_url]
    dl_url = lst_link[count - 1]
    dl_url = dl_url.replace(" ", "%20")
    return dl_url


def filesIm(url):
    return Bypass().bypass_filesIm(url)


def gdbot(url):
    client = cloudscraper.create_scraper(allow_brotli=False)
    resp = client.get(url)
    gdtot_url = re.findall('mb-2" href="(.*?)" target="_blank"', resp.text)
    url = gdtot_url[0]
    resp = client.get(url)
    token = re.findall("'token', '(.*?)'", resp.text)[0]
    data = {"token": token}
    resp2 = client.post(url, data=data).text
    res = resp2.split('":"')[1].split('"}')[0].replace("\\", "")
    return res


def github(url):
    download = requests.get(url, stream=True, allow_redirects=False)
    return download.headers["location"]


def gofile(url):
    api_uri = "https://api.gofile.io"
    client = cloudscraper.create_scraper(allow_brotli=False)
    res = client.get(f"{api_uri}/createAccount").json()
    data = {
        "contentId": url.split("/")[-1],
        "token": res["data"]["token"],
        "websiteToken": 12345,
        "cache": "true",
    }
    res = client.get(f"{api_uri}/getContent", params=data).json()
    for item in res["data"]["contents"].values():
        content = item
        dl_url = content["directLink"]
        dl_url = dl_url.replace(" ", "%20")
        return dl_url


def hxfile(url):
    return Bypass().bypass_filesIm(url)


def krakenfiles(url):
    page_resp = requests.session().get(url)
    soup = BeautifulSoup(page_resp.text, "lxml")
    token = soup.find("input", id="dl-token")["value"]
    hashes = [
        item["data-file-hash"]
        for item in soup.find_all("div", attrs={"data-file-hash": True})
    ]
    if not hashes:
        return f"Hash not found for : {url}"
    dl_hash = hashes[0]
    payload = f'------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name="token"\r\n\r\n{token}\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--'
    headers = {
        "content-type": "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        "cache-control": "no-cache",
        "hash": dl_hash,
    }
    dl_link_resp = requests.session().post(
        f"https://krakenfiles.com/download/{hash}", data=payload, headers=headers
    )
    dl_link_json = dl_link_resp.json()
    dl_url = dl_link_json["url"]
    dl_url = dl_url.replace(" ", "%20")
    return dl_url


def letsupload(url):
    return Bypass().bypass_url(url)


def linkpoi(url):
    return Bypass().bypass_linkpoi(url)


def mdisk(url):
    check = re.findall(r"\bhttps?://.*mdisk\S+", url)
    link = check[0]
    url = link.split("/")[-1]
    scraper = cloudscraper.create_scraper(interpreter="nodejs", allow_brotli=False)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }
    api = f"https://diskuploader.entertainvideo.com/v1/file/cdnurl?param={url}"
    response = scraper.get(api, headers=headers).json()
    dl_url = response["download"]
    dl_url = dl_url.replace(" ", "%20")
    return dl_url


def mediafire(url):
    page = BeautifulSoup(requests.get(url).content, "lxml")
    info = page.find("a", {"aria-label": "Download file"})
    dl_url = info.get("href")
    dl_url = dl_url.replace(" ", "%20")
    return dl_url


def megaup(url):
    client = cloudscraper.create_scraper(allow_brotli=False)
    resp = client.get(url)
    data = (
        resp.text.split("DeObfuscate_String_and_Create_Form_With_Mhoa_URL(", 2)[2]
        .split(");")[0]
        .split(",")
    )
    data = [a.strip("' ") for a in data]
    time.sleep(3)
    idurl = "".join(data[0][i] for i in range(len(data[0]) // 4 - 1, -1, -1))
    for i in range(int(len(data[0]) / 4 * 3 - 1), int(len(data[0]) / 4 * 2) - 1, -1):
        idurl += data[0][i]
    for i in range(int((len(data[1]) - 3) / 2 + 2), 2, -1):
        idurl += data[1][i]
        des_url = f"https://download.megaup.net/?idurl={idurl}&idfilename={data[2]}&idfilesize={data[3]}"
        des_url = des_url.replace(" ", "%20")
        return des_url


def mirrored(url):
    return Bypass().bypass_mirrored(url)


def osdn(url):
    link = re.findall(r"\bhttps?://.*osdn\.net\S+", url)[0]
    page = BeautifulSoup(requests.get(link, allow_redirects=True).content, "lxml")
    info = page.find("a", {"class": "mirror_link"})
    link = urllib.parse.unquote("https://osdn.net" + info["href"])
    mirrors = page.find("form", {"id": "mirror-select-form"}).findAll("tr")
    urls = []
    for data in mirrors[1:]:
        mirror = data.find("input")["value"]
        urls.append(re.sub(r"m=(.*)&f", f"m={mirror}&f", link))
    return urls[0]


def pandafile(url):
    id_p = re.compile("pandafiles.com/(.+?)/")
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://pandafiles.com",
        "Referer": "https://pandafiles.com/",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Te": "trailers",
    }
    id = re.findall(id_p, url)[0]
    data = {
        "op": "download2",
        "usr_login": "",
        "id": id,
        "rand": "",
        "referer": url,
        "method_free": "Free Download",
        "method_premium": "",
        "adblock_detected": "0",
    }
    resp = requests.post(url, headers=headers, data=data)
    bsObj = BeautifulSoup(resp.content, features="lxml")
    for a in bsObj.find_all("a", href=True):
        dl_url = a["href"]
        dl_url = dl_url.replace(" ", "%20")
        return dl_url


def pixeldrain(url):
    url = url.strip("/ ")
    file_id = url.split("/")[-1]
    if url.split("/")[-2] == "l":
        info_link = f"https://pixeldrain.com/api/list/{file_id}"
        dl_link = f"https://pixeldrain.com/api/list/{file_id}/zip"
    else:
        info_link = f"https://pixeldrain.com/api/file/{file_id}/info"
        dl_link = f"https://pixeldrain.com/api/file/{file_id}"
    dl_link = dl_link.replace(" ", "%20")
    return dl_link


def pixl(url):
    resp = requests.get(url)
    currentpage = 1
    settotalimgs = True
    totalimages = ""
    soup = BeautifulSoup(resp.content, "html.parser")
    if "album" in url and settotalimgs:
        totalimages = soup.find("span", {"data-text": "image-count"}).text
        settotalimgs = False
    thmbnailanchors = soup.findAll(attrs={"class": "--media"})
    links = soup.findAll(attrs={"data-pagination": "next"})
    try:
        url = links[0].attrs["href"]
    except BaseException:
        url = None
    count = 1
    ddl_msg = ""
    for ref in thmbnailanchors:
        imgdata = requests.get(ref.attrs["href"])
        if not imgdata.status_code == 200:
            time.sleep(3)
            continue
        imghtml = BeautifulSoup(imgdata.text, "html.parser")
        downloadanch = imghtml.find(attrs={"class": "btn-download"})
        currentimg = downloadanch.attrs["href"]
        ddl_msg += f"<b>{count}.</b> <code>{currentimg}</code><br>"
        count += 1
    currentpage += 1
    fld_msg = f"<b><i>Your provided Pixl.is link is of Folder and I've Found {count - 1} files in the folder.</i></b><br>"
    fld_msg += f"<i>I've generated Direct Links for all the files.</i><br><br>"
    tlg_url = telegraph_paste(fld_msg + ddl_msg)
    return tlg_url


def reupload(url):
    return Bypass().bypass_reupload(url)


def sbembed(url):
    dl_url = Bypass().bypass_sbembed(url)
    count = len(dl_url)
    lst_link = [dl_url[i] for i in dl_url]
    dl_url = lst_link[count - 1]
    dl_url = dl_url.replace(" ", "%20")
    return dl_url


def is_sendcm_folder_link(url: str):
    return (
        "https://send.cm/s/" in url
        or "https://send.cm/?sort" in url
        or "https://send.cm/?sort_field" in url
        or "https://send.cm/?sort_order" in url
    )


def sendcm(url):
    base_url = "https://send.cm/"
    client = cloudscraper.create_scraper(allow_brotli=False)
    hs = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    }
    is_sendcm_folder = is_sendcm_folder_link(url)
    if is_sendcm_folder:
        done = False
        msg = ""
        page_no = 0
        while not done:
            page_no += 1
            resp = client.get(url)
            soup = BeautifulSoup(resp.content, "lxml")
            table = soup.find("table", id="xfiles")
            files = table.find_all("a", class_="tx-dark")
            for file in files:
                file_url = file["href"]
                resp2 = client.get(file_url)
                scrape = BeautifulSoup(resp2.text, "html.parser")
                inputs = scrape.find_all("input")
                file_id = inputs[1]["value"]
                file_name = re.findall("URL=(.*?) - ", resp2.text)[0].split("]")[1]
                parse = {"op": "download2", "id": file_id, "referer": url}
                resp3 = client.post(
                    base_url, data=parse, headers=hs, allow_redirects=False
                )
                dl_url = resp3.headers["Location"]
                dl_url = dl_url.replace(" ", "%20")
                msg += f"<b>File Name:</b> {file_name}<br><b>File Link:</b> <code>{file_url}</code><br><b>Download Link:</b> <code>{dl_url}</code><br>"
                pages = soup.find("ul", class_="pagination")
                if pages is None:
                    done = True
                else:
                    current_page = pages.find(
                        "li", "page-item actived", recursive=False
                    )
                    next_page = current_page.next_sibling
                    if next_page is None:
                        done = True
                    else:
                        url = base_url + next_page["href"]
        tlg_url = telegraph_paste(msg)
        return tlg_url
    else:
        resp = client.get(url)
        scrape = BeautifulSoup(resp.text, "html.parser")
        inputs = scrape.find_all("input")
        file_id = inputs[1]["value"]
        file_name = re.findall("URL=(.*?) - ", resp.text)[0].split("]")[1]
        parse = {"op": "download2", "id": file_id, "referer": url}
        resp2 = client.post(base_url, data=parse, headers=hs, allow_redirects=False)
        dl_url = resp2.headers["Location"]
        dl_url = dl_url.replace(" ", "%20")
        msg = f"<b>File Name:</b> {file_name}<br><b>File Link:</b> <code>{url}</code><br><b>Download Link:</b> <code>{dl_url}</code><br>"
        tlg_url = telegraph_paste(msg)
        return tlg_url


def solidfiles(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36"
    }
    pageSource = requests.get(url, headers=headers).text
    mainOptions = str(re.search(r"viewerOptions\'\,\ (.*?)\)\;", pageSource).group(1))
    return json.loads(mainOptions)["downloadUrl"]


def sfile(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.1; SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3239.83 Mobile Safari/537.36"
    }
    url3 = BeautifulSoup(requests.get(url, headers=headers).content, "html.parser")
    dl_url = url3.find("a", "w3-button w3-blue")["href"]
    dl_url = dl_url.replace(" ", "%20")
    return dl_url


def sourceforge(url):
    link = re.findall(r"\bhttps?://sourceforge\.net\S+", url)[0]
    file_path = re.findall(r"files(.*)/download", link)[0]
    project = re.findall(r"projects?/(.*?)/files", link)[0]
    mirrors = (
        f"https://sourceforge.net/settings/mirror_choices?"
        f"projectname={project}&filename={file_path}"
    )
    page = BeautifulSoup(requests.get(mirrors).content, "html.parser")
    info = page.find("ul", {"id": "mirrorList"}).findAll("li")
    for mirror in info[1:]:
        return f'https://{mirror["id"]}.dl.sourceforge.net/project/{project}/{file_path}?viasf=1'


def streamlare(url):
    CONT_ID = re.compile(r"/[ve]/([^?#&/]+)")
    api = "https://streamlare.com/api/video/download/get"
    client = cloudscraper.create_scraper(allow_brotli=False)
    cont_id = CONT_ID.search(url)[1]
    r = client.get(url).text
    soup = BeautifulSoup(r, "html.parser")
    csrf_token = soup.find("meta", {"name": "csrf-token"}).get("content")
    xsrf_token = client.cookies.get_dict()["XSRF-TOKEN"]
    headers = {
        "x-requested-with": "XMLHttpRequest",
        "x-csrf-token": csrf_token,
        "x-xsrf-token": xsrf_token,
    }
    data = {"id": cont_id}
    res = client.post(api, headers=headers, data=data).json()
    res = res.replace(" ", "%20")
    return res


def streamtape(url):
    return Bypass().bypass_streamtape(url)


def uploadee(url):
    soup = BeautifulSoup(requests.get(url).content, "lxml")
    sa = soup.find("a", attrs={"id": "d_l"})
    return sa["href"]


def uservideo(url):
    return Bypass().bypass_uservideo(url)


def wetransfer(url):
    if url.startswith("https://we.tl/"):
        r = requests.head(url, allow_redirects=True)
        url = r.url
    recipient_id = None
    params = urllib.parse.urlparse(url).path.split("/")[2:]
    if len(params) == 2:
        transfer_id, security_hash = params
    elif len(params) == 3:
        transfer_id, recipient_id, security_hash = params
    else:
        return None
    j = {
        "intent": "entire_transfer",
        "security_hash": security_hash,
    }
    if recipient_id:
        j["recipient_id"] = recipient_id
    s = cloudscraper.create_scraper(allow_brotli=False)
    r = s.get("https://wetransfer.com/")
    m = re.search('name="csrf-token" content="([^"]+)"', r.text)
    s.headers.update({"x-csrf-token": m[1], "x-requested-with": "XMLHttpRequest"})
    r = s.post(
        f"https://wetransfer.com/api/v4/transfers/{transfer_id}/download", json=j
    )
    j = r.json()
    dl_url = j["direct_link"]
    dl_url = dl_url.replace(" ", "%20")
    return dl_url


def yandex_disk(url):
    link = re.findall(
        r"\b(https?://(yadi.sk|disk.yandex.com|disk.yandex.ru|disk.yandex.com.tr|disk.yandex.com.ru)\S+)",
        url,
    )[0][0]
    api = "https://cloud-api.yandex.net/v1/disk/public/resources/download?public_key={}"
    dl_url = requests.get(api.format(link)).json()["href"]
    dl_url = dl_url.replace(" ", "%20")
    return dl_url


def zippyshare(url):
    return Bypass().bypass_zippyshare(url)
