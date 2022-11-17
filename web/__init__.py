import logging

from flask import Flask
from flask_restful import Api

logging.basicConfig(
    format="%(asctime)s - [%(filename)s:%(lineno)d] - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("flask").setLevel(logging.WARNING)
logging.getLogger("flask_restful").setLevel(logging.WARNING)


from web.scripts.bypass import (adfly, adrinolinks, bifm, droplink, dulink,
                                gplinks, gtlinks, gyanilinks, htpmovies,
                                hypershort, linkvertise, multi_aio, ouo, pkin,
                                privatemoviez, rewayatcafe, rocklinks,
                                script_a, script_b, shareus, short2url, shorte,
                                shortingly, shortly, sirigan, thinfi, tnlink,
                                xpshort)
from web.scripts.direct import (androiddatahost, anonfiles, antfiles,
                                artstation, bunkr_cyber, dropbox, fembed,
                                filesIm, gdbot, github, gofile, hxfile,
                                krakenfiles, letsupload, linkpoi, mdisk,
                                mdisk_mpd, mediafire, megaup, mirrored,
                                mp4upload, osdn, pandafile, pixeldrain, pixl,
                                reupload, sbembed, sendcm, sfile, solidfiles,
                                sourceforge, streamlare, streamsb, streamtape,
                                uploadbaz, uploadee, uppit, userscloud,
                                uservideo, wetransfer, yandex_disk, zippyshare)
from web.scripts.misc import (dictionary_search, github_search, google_search,
                              image_search, lyrics_search, npm_search,
                              pypi_search, reddit_search, spellcheck,
                              stackoverflow_search, tgsticker_search,
                              tmdb_search, torrent_search, unsplash_search,
                              urban_search, wiki_search, xda_search,
                              youtube_search)
from web.scripts.pasting import telegraph_paste
from web.scripts.scraper import (atishmkv_scrape, cinevez_scrape,
                                 cinevood_scrape, filecrypt_scrape,
                                 htpmovies_scrape, igggames_scrape,
                                 index_scrape, magnet_scrape,
                                 moviesdrama_scrape, olamovies_scrape,
                                 privatemoviez_scrape, psa_scrape,
                                 sharespark_scrape, toonworld4all_scrape)
from web.scripts.shorten import (bitly_shorten, clckru_shorten, clilp_shorten,
                                 dagd_shorten, isgd_shorten, osdb_shorten,
                                 tinyurl_shorten, ttm_shorten, vgd_shorten)

BYP_SUP_SITES = {
    "adfly": adfly,
    "adrinolinks": adrinolinks,
    "bifm": bifm,
    "droplink": droplink,
    "dulink": dulink,
    "gplinks": gplinks,
    "gtlinks": gtlinks,
    "gyanilinks": gyanilinks,
    "htpmovies": htpmovies,
    "hypershort": hypershort,
    "linkvertise": linkvertise,
    "multi_aio": multi_aio,
    "ouo": ouo,
    "privatemoviez": privatemoviez,
    "pkin": pkin,
    "rewayatcafe": rewayatcafe,
    "rocklinks": rocklinks,
    "script_a": script_a,
    "script_b": script_b,
    "shareus": shareus,
    "shorte": shorte,
    "short2url": short2url,
    "shortingly": shortingly,
    "shortly": shortly,
    "sirigan": sirigan,
    "thinfi": thinfi,
    "tnlink": tnlink,
    "xpshort": xpshort,
}

DIRT_SUP_SITES = {
    "androiddatahost": androiddatahost,
    "anonfiles": anonfiles,
    "antfiles": antfiles,
    "artstation": artstation,
    "dropbox": dropbox,
    "fembed": fembed,
    "filesIm": filesIm,
    "gdbot": gdbot,
    "github": github,
    "gofile": gofile,
    "hxfile": hxfile,
    "krakenfiles": krakenfiles,
    "letsupload": letsupload,
    "linkpoi": linkpoi,
    "mdisk": mdisk,
    "mdisk_mpd": mdisk_mpd,
    "mediafire": mediafire,
    "megaup": megaup,
    "mp4upload": mp4upload,
    "mirrored": mirrored,
    "osdn": osdn,
    "pandafile": pandafile,
    "pixeldrain": pixeldrain,
    "reupload": reupload,
    "sbembed": sbembed,
    "solidfiles": solidfiles,
    "sfile": sfile,
    "sourceforge": sourceforge,
    "streamsb": streamsb,
    "streamlare": streamlare,
    "streamtape": streamtape,
    "uploadbaz": uploadbaz,
    "uploadee": uploadee,
    "uppit": uppit,
    "userscloud": userscloud,
    "uservideo": uservideo,
    "wetransfer": wetransfer,
    "yandex_disk": yandex_disk,
    "zippyshare": zippyshare,
    "bunkr_cyber": bunkr_cyber,
    "pixl": pixl,
    "sendcm": sendcm,
}

MISC_SUP_SITES = {
    "wiki_search": wiki_search,
    "xda_search": xda_search,
    "youtube_search": youtube_search,
    "dictionary_search": dictionary_search,
    "google_search": google_search,
    "github_search": github_search,
    "image_search": image_search,
    "lyrics_search": lyrics_search,
    "npm_search": npm_search,
    "pypi_search": pypi_search,
    "reddit_search": reddit_search,
    "spellcheck": spellcheck,
    "tgsticker_search": tgsticker_search,
    "stackoverflow_search": stackoverflow_search,
    "torrent_search": torrent_search,
    "tmdb_search": tmdb_search,
    "urban_search": urban_search,
    "unsplash_search": unsplash_search,
}

PASTE_SUP_SITES = {
    "telegraph_paste": telegraph_paste,
}

SCRAPE_SUP_SITES = {
    "filecrypt_scrap": filecrypt_scrape,
    "index_scrap": index_scrape,
    "psa_scrap": psa_scrape,
    "olamovies_scrap": olamovies_scrape,
    "igggames_scrap": igggames_scrape,
    "magnet_scrap": magnet_scrape,
    "toonworld4all_scrap": toonworld4all_scrape,
    "atishmkv_scrap": atishmkv_scrape,
    "moviesdrama_scrap": moviesdrama_scrape,
    "cinevood_scrap": cinevood_scrape,
    "cinevez_scrap": cinevez_scrape,
    "htpmovies_scrap": htpmovies_scrape,
    "sharespark_scrap": sharespark_scrape,
    "privatemoviez_scrap": privatemoviez_scrape,
}

SHRT_SUP_SITES = {
    "bitly_shorten": bitly_shorten,
    "dagd_shorten": dagd_shorten,
    "tinyurl_shorten": tinyurl_shorten,
    "osdb_shorten": osdb_shorten,
    "ttm_shorten": ttm_shorten,
    "isgd_shorten": isgd_shorten,
    "vgd_shorten": vgd_shorten,
    "clckru_shorten": clckru_shorten,
    "clilp_shorten": clilp_shorten,
}

app = Flask(__name__)
abc = Api(app)
