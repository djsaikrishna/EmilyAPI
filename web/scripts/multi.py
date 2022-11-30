import PyBypass

from web.helpers.lists import *
from web.scripts.bypass import *
from web.scripts.direct import *
from web.scripts.scraper import *


async def all_in_one(url):
    is_artstation = is_artstation_link(url)
    if "droplink." in url or "droplinks." in url:
        res = await droplink(url)
    elif "dulink." in url:
        res = await dulink(url)
    elif "gplink." in url or "gplinks." in url:
        res = await gplinks(url)
    elif any(x in url for x in linkvertise_list):
        res = await linkvertise(url)
    elif any(x in url for x in adfly_list):
        res = await adfly(url)
    elif "htpmovies." in url and "/exit.php?url" in url:
        res = await htpmovies(url)
    elif "privatemoviez." in url and "/secret?data=" in url:
        res = await privatemoviez(url)
    elif "hypershort." in url:
        res = await hypershort(url)
    elif "ez4short." in url:
        res = await ez4short(url)
    elif "sirigan.my.id" in url:
        res = await sirigan(url)
    elif "ouo.io" in url or "ouo.press" in url:
        res = await ouo(url)
    elif any(x in url for x in shst_list):
        res = await shorte(url)
    elif "rocklinks." in url:
        res = await rocklinks(url)
    elif ("gtlinks." or "loan.kinemaster.cc/?token=" or "theforyou.in/?token=") in url:
        url = url.replace("&m=1", "")
        res = await gtlinks(url)
    elif "gyanilinks." in url:
        res = await gyanilinks(url)
    elif "shareus." in url:
        res = await shareus(url)
    elif "short2url." in url:
        res = await short2url(url)
    elif "krownlinks." in url:
        res = await krownlinks(url)
    elif "shortingly." in url:
        res = await shortingly(url)
    elif "try2link." in url:
        res = await try2link(url)
    elif "tnlink." in url:
        res = await tnlink(url)
    elif "urlsopen." in url:
        res = await urlsopen(url)
    elif "xpshort." in url:
        res = await xpshort(url)
    elif "adrinolinks." in url:
        res = await adrinolinks(url)
    elif "pkin." in url:
        res = await pkin(url)
    elif "shortly." in url:
        res = await shortly(url)
    elif "thinfi." in url:
        res = await thinfi(url)
    elif is_artstation:
        res = await artstation(url)
    elif "mdisk." in url:
        res = await mdisk(url)
    elif "wetransfer." in url or "we.tl" in url:
        res = await wetransfer(url)
    elif "gdbot." in url:
        res = await gdbot(url)
    elif "gofile." in url:
        # res = await gofile(url)
        res = await url  # Temporary Solution
    elif "megaup." in url:
        res = await megaup(url)
    elif "mcloud." in url:
        res = await mycloud(url)
    elif "sfile.mobi" in url:
        res = await sfile(url)
    elif any(x in url for x in yandisk_list):
        res = await yandex_disk(url)
    elif "osdn." in url:
        res = await osdn(url)
    elif "github.com" in url:
        res = await github(url)
    elif "mediafire." in url:
        res = await mediafire(url)
    elif "zippyshare." in url:
        res = await zippyshare(url)
    elif "hxfile." in url:
        res = await hxfile(url)
    elif "files.im" in url:
        res = await filesIm(url)
    elif "anonfiles." in url:
        res = await anonfiles(url)
    elif "letsupload." in url:
        res = await letsupload(url)
    elif "linkpoi." in url:
        res = await linkpoi(url)
    elif any(x in url for x in fmed_list):
        res = await fembed(url)
    elif any(x in url for x in sbembed_list):
        res = await sbembed(url)
    elif "mirrored." in url:
        res = await mirrored(url)
    elif "reupload." in url:
        res = await reupload(url)
    elif "uservideo." in url:
        res = await uservideo(url)
    elif "videovard." in url:
        res = await videovard(url)
    elif ("vidstreamz" or "vidstream" or "vizcloud2.") in url:
        res = await vidstream(url)
    elif "antfiles." in url:
        res = await antfiles(url)
    elif "streamtape." in url:
        res = await streamtape(url)
    elif "sourceforge." in url:
        res = await sourceforge(url)
    elif "androidatahost." in url:
        res = await androiddatahost(url)
    elif "krakenfiles." in url:
        res = await krakenfiles(url)
    elif "dropbox." in url:
        res = await dropbox(url)
    elif "pixeldrain." in url:
        res = await pixeldrain(url)
    elif ("streamlare." or "sltube.") in url:
        res = await streamlare(url)
    elif "pandafiles." in url:
        res = await pandafile(url)
    elif "upload.ee" in url:
        res = await uploadee(url)
    elif "solidfiles." in url:
        res = await solidfiles(url)
    elif "adrinolinks." in url:
        res = await adrinolinks(url)
    elif "dropbox." in url:
        res = await dropbox(url)
    elif "mp4upload." in url:
        res = await mp4upload(url)
    elif ("streamsb." or "watchsb.") in url:
        res = await streamsb(url)
    elif "uploadbaz." in url:
        res = await uploadbaz(url)
    elif "uppit." in url:
        res = await uppit(url)
    elif "userscloud." in url:
        res = await userscloud(url)
    elif (
        "workers.dev" in url
        or "0:/" in url
        or "1:/" in url
        or "2:/" in url
        or "3:/" in url
        or "4:/" in url
        or "5:/" in url
        or "6:/" in url
    ):
        res = await index_scrape(url)
    elif "atishmkv." in url or "atish.mkv" in url:
        res = await atishmkv_scrape(url)
    elif "cinevez." in url:
        res = await cinevez_scrape(url)
    elif "cinevood." in url:
        res = await cinevood_scrape(url)
    elif "filecrypt." in url:
        res = await filecrypt_scrape(url)
    elif "htpmovies." in url and "/exit.php?url=" in url:
        res = await htpmovies(url)
    elif "igg-games." in url:
        res = await igggames_scrape(url)
    elif "animeremux." in url:
        res = await animeremux_scrape(url)
    elif "moviesdrama." in url:
        res = await moviesdrama_scrape(url)
    elif "olamovies." in url:
        res = await olamovies_scrape(url)
    elif "psa." in url:
        res = await psa_scrape(url)
    elif "taemovies." in url:
        res = await taemovies_scrape(url)
    elif "teleguflix." in url:
        res = await teleguflix_scrape(url)
    elif "toonworld4all." in url:
        res = await toonworld4all_scrape(url)
    elif "sharespark." in url:
        res = await sharespark_scrape(url)
    elif "privatemoviez." in url and "/secret?data=" in url:
        res = await privatemoviez(url)
    else:
        res = PyBypass.bypass(url)
    return res
