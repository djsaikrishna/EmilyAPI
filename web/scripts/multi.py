import PyBypass

from web.helpers.lists import *
from web.scripts.bypass import *
from web.scripts.direct import *
from web.scripts.scraper import *


def all_in_one(url):
    is_artstation = is_artstation_link(url)
    if "droplink." in url or "droplinks." in url:
        res = droplink(url)
    elif "dulink." in url:
        res = dulink(url)
    elif "gplink." in url or "gplinks." in url:
        res = gplinks(url)
    elif any(x in url for x in linkvertise_list):
        res = linkvertise(url)
    elif any(x in url for x in adfly_list):
        res = adfly(url)
    elif "htpmovies." in url and "/exit.php?url" in url:
        res = htpmovies(url)
    elif "privatemoviez." in url and "/secret?data=" in url:
        res = privatemoviez(url)
    elif "hypershort." in url:
        res = hypershort(url)
    elif "ez4short." in url:
        res = ez4short(url)
    elif "sirigan.my.id" in url:
        res = sirigan(url)
    elif "ouo.io" in url or "ouo.press" in url:
        res = ouo(url)
    elif any(x in url for x in shst_list):
        res = shorte(url)
    elif "rocklinks." in url:
        res = rocklinks(url)
    elif ("gtlinks." or "loan.kinemaster.cc/?token=" or "theforyou.in/?token=") in url:
        url = url.replace("&m=1", "")
        res = gtlinks(url)
    elif "gyanilinks." in url:
        res = gyanilinks(url)
    elif "shareus." in url:
        res = shareus(url)
    elif "short2url." in url:
        res = short2url(url)
    elif "krownlinks." in url:
        res = krownlinks(url)
    elif "shortingly." in url:
        res = shortingly(url)
    elif "try2link." in url:
        res = try2link(url)
    elif "tnlink." in url:
        res = tnlink(url)
    elif "xpshort." in url:
        res = xpshort(url)
    elif "adrinolinks." in url:
        res = adrinolinks(url)
    elif "pkin." in url:
        res = pkin(url)
    elif "shortly." in url:
        res = shortly(url)
    elif "thinfi." in url:
        res = thinfi(url)
    elif is_artstation:
        res = artstation(url)
    elif "mdisk." in url:
        res = mdisk(url)
        mdisk_mpd(url)
    elif "wetransfer." in url or "we.tl" in url:
        res = wetransfer(url)
    elif "gdbot." in url:
        res = gdbot(url)
    elif "gofile." in url:
        # res = gofile(url)
        res = url  # Temporary Solution
    elif "megaup." in url:
        res = megaup(url)
    elif "sfile.mobi" in url:
        res = sfile(url)
    elif any(x in url for x in yandisk_list):
        res = yandex_disk(url)
    elif "osdn." in url:
        res = osdn(url)
    elif "github.com" in url:
        res = github(url)
    elif "mediafire." in url:
        res = mediafire(url)
    elif "zippyshare." in url:
        res = zippyshare(url)
    elif "hxfile." in url:
        res = hxfile(url)
    elif "files.im" in url:
        res = filesIm(url)
    elif "anonfiles." in url:
        res = anonfiles(url)
    elif "letsupload." in url:
        res = letsupload(url)
    elif "linkpoi." in url:
        res = linkpoi(url)
    elif any(x in url for x in fmed_list):
        res = fembed(url)
    elif any(x in url for x in sbembed_list):
        res = sbembed(url)
    elif "mirrored." in url:
        res = mirrored(url)
    elif "reupload." in url:
        res = reupload(url)
    elif "uservideo." in url:
        res = uservideo(url)
    elif "antfiles." in url:
        res = antfiles(url)
    elif "streamtape." in url:
        res = streamtape(url)
    elif "sourceforge." in url:
        res = sourceforge(url)
    elif "androidatahost." in url:
        res = androiddatahost(url)
    elif "krakenfiles." in url:
        res = krakenfiles(url)
    elif "dropbox." in url:
        res = dropbox(url)
    elif "pixeldrain." in url:
        res = pixeldrain(url)
    elif ("streamlare." or "sltube.") in url:
        res = streamlare(url)
    elif "pandafiles." in url:
        res = pandafile(url)
    elif "upload.ee" in url:
        res = uploadee(url)
    elif "solidfiles." in url:
        res = solidfiles(url)
    elif "adrinolinks." in url:
        res = adrinolinks(url)
    elif "dropbox." in url:
        res = dropbox(url)
    elif "mp4upload." in url:
        res = mp4upload(url)
    elif ("streamsb." or "watchsb.") in url:
        res = streamsb(url)
    elif "uploadbaz." in url:
        res = uploadbaz(url)
    elif "uppit." in url:
        res = uppit(url)
    elif "userscloud." in url:
        res = userscloud(url)
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
        res = index_scrape(url)
    elif "atishmkv." in url or "atish.mkv" in url:
        res = atishmkv_scrape(url)
    elif "cinevez." in url:
        res = cinevez_scrape(url)
    elif "cinevood." in url:
        res = cinevood_scrape(url)
    elif "filecrypt." in url:
        res = filecrypt_scrape(url)
    elif "htpmovies." in url and "/exit.php?url=" in url:
        res = htpmovies(url)
    elif "igg-games." in url:
        res = igggames_scrape(url)
    elif "animeremux." in url:
        res = animeremux_scrape(url)
    elif "moviesdrama." in url:
        res = moviesdrama_scrape(url)
    elif "olamovies." in url:
        res = olamovies_scrape(url)
    elif "psa." in url:
        res = psa_scrape(url)
    elif "taemovies." in url:
        res = taemovies_scrape(url)
    elif "teleguflix." in url:
        res = teleguflix_scrape(url)
    elif "toonworld4all." in url:
        res = toonworld4all_scrape(url)
    elif "sharespark." in url:
        res = sharespark_scrape(url)
    elif "privatemoviez." in url and "/secret?data=" in url:
        res = privatemoviez(url)
    else:
        res = PyBypass.bypass(url)
    return res
