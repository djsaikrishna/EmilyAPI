# Emily`s API (written in Flask)

<b><i>Emily API Server that integrates various scripts and processes them server-side (written in Flask)</i></b><br>

## Usage

### Environment Variables
1. Set the Server Port to use in `PORT`.It defaults to 8080 and this variable only works for Python Deployment.
2. Set the BIFM API URL to use for Bypass in `BIFM_URL`. It defaults to this [API](https://bifm.tacohitbox.com/api/bypass?url).
3. Set the SAFONE API URL to use in `SAFONE_API_URL`. It defaults to this [API](https://api.safone.tech/).
4. Set the Telegraph Name to use in `TELEGRAPH_NAME`. It defaults to this Name - EmilyAPI.
5. Set the Telegraph URL to use in `TELEGRAPH_LINK`. It defaults to this [link](https://github.com/missemily22).
6. (Optional) Set `DATABASE_URL` to a MongoDB URL (Connection string) for storing/obtaining results generated via the /api/bypass and /api/direct endpoints.<br>
Follow this [guide](/README.md#generate-database) to generate database. 
7. (Optional) Set `WARP_ID` to your Cloudflare Warp ID if you want to generate some extra Warp+ Quota

### Starting the Server

A. Python
1. Install the required python packages using `pip install -r requirements.txt`
2. Start the server using `python -m web` or `python3 -m web`
3. The server will start at port 8080 (By Default)

B. DockerFile
1. Build the Docker Image first using `sudo docker build . -t emily-api`
2. Then run the Docker Image using `sudo docker run -p 8080:8080 emily-api`
3. To stop the Docker , use `sudo docker ps` and `sudo docker stop {name/id}`

C. Docker Compose
1. Build and run the Image using `sudo docker-compose up`
2. After Editing Files, Run `sudo docker-compose up --build` to rebuild the image
3. To Stop the Image, Use `sudo docker-compose stop`
4. To Start the Image again, Use `sudo docker-compose start`

### Making Requests

1. You can make `POST` as well as `GET` requests to the server
2. Server Endpoints are - 
    1. `/api/bypass` for AD-Bypassers
    2. `/api/direct` for DL-Generators
    3. `/api/misc` for Misc Services
    4. `/api/paste` for Pasting
    5. `/api/scraper` for Site Scraping
    6. `/api/shorten` for Link Shorteners
    7. `/api/multi` for all Bypassers, Generators and Scrapers combined
3. The data should be in json format and should have two of these keys:
    1. `type` - Specify Link Bypasser/Direct-Gen Type to use
    2. `url` - Specify the link which is to be sent to Bypass/Direct-Link (This Key is not for Paste & Misc Services)
	3. `text` - Specify the text which is to be sent for pasting (This Key is only for Paste)
	3. `query` - Specify the word(s) for misc services (This Key is only for Misc Services)
4. The Returned Json Data has a Field `success` (boolean) specifying if the Request was Successful or not
5. In Case of Error,`success` is False and a Field `msg` is returned containing the Error
6. Otherwise `success` is True and a Key `url` contains the Bypassed Link


## Important Points

1. MegaUP Download URLs can only be downloaded by Non-Blacklisted IPs as their server is Cloudflare Protected.
2. If you do not want to use Environment Variables, then you can manually change them in 
    1. [bypass.py](web/scripts/bypass.py) in L11
    2. [misc.py](web/scripts/misc.py) in L4
    3. [telegraph_helper.py](web/scripts/telegraph_helper.py) in L11 & L12
3. The default Telegraph URL that this API uses is gra.ph (And not telegra.ph !)
4. Results for Bunkr, CybderDrop, Pixl & SendCM as well FileCrypt, Bhadoo Index & Psa.pm Scraper will be in Telegraph URLs.
5. Psa Scraper does not work anymore as of 16/10/2022. Still I kept it since I hope the script will be updated soon.
6. Both the Scripts `script_a` and `script_b` are added for bypassing for adlinks which share similar working. Examples - [1](https://link.mdisk.website/Pnms055v) & [2](https://xpshort.com/9DNKf).
7. Only use 'url' key for making requests to multifunction API Endpoint. The server is meant to autodetect desired function.
8. The warp script at [warp.py](/warp.py) is just there for fun. If you want then you can add your own Warp ID there or leave it for mine :p

### Generate Database

1. Go to `https://mongodb.com/` and sign-up.
2. Create Shared Cluster.
3. Press on `Database` under `Deployment` Header, your created cluster will be there.
5. Press on connect, choose `Allow Access From Anywhere` and press on `Add IP Address` - Put '0.0.0.0', then create user.
6. After creating user press on `Choose a connection`, then press on `Connect your application`. Choose `Driver` **python** and `version` **3.6 or later**.
7. Copy your `connection string` and replace `<password>` with the password of your user, then press close.


## Available Link Bypassers

* The following bypassers (with corresponding types) are supported:

| S.No. | Bypasser        | Type          |
|-------|-----------------|---------------|
| 1.    | AdFly           | `adfly`       |
| 2.    | AdrinoLinks     | `adrinolinks` |
| 3.    | BIFM API        | `bifm`        |
| 4.    | DropLink        | `droplink`    |
| 5.    | GpLink          | `gplinks`     |
| 6.    | GTLinks         | `gtlinks`     |
| 7.    | GyaniLinks      | `gyanilinks`  |
| 8.    | HTPMovies       | `htpmovies`   |
| 9.    | Hypershort      | `hypershort`  |
| 10.   | Linkvertise     | `linkvertise` |
| 11.   | Bypass.vip API  | `multi_aio`   |
| 12.   | Ouo             | `ouo`         |
| 13.   | PrivateMoviez   | `privatemoviez` |
| 14.   | RewayatCafe     | `rewayatcafe` |
| 15.   | RockLinks       | `rocklinks`   |
| 16.   | Script - A      | `script_a`    |
| 17.   | Script - B      | `script_b`    |
| 18.   | ShareUs         | `shareus`     |
| 19.   | Shorte          | `shorte`      |
| 20.   | Shortingly      | `shortingly`  |
| 21.   | Sirigan         | `sirigan`     |
| 22.   | TnLink          | `tnlink`      |
| 23.   | Xpshort         | `xpshort`     |
| 24.   | Pkin            | `pkin`        |
| 25.   | Shortly         | `shortly`     |
| 26.   | Thinfi          | `thinfi`      |
| 27.   | Short2url       | `short2url`   |
| 28.   | Dulink          | `dulink`      |
| 29.   | Ez4Short        | `ez4short`    |
| 30.   | Try2Link        | `try2link`    |
| 31.   | URLsOpen        | `urlsopen`    |
| 32.   | LinkBnao        | `linkbnao`    |
| 33.   | MdiskPro        | `mdiskpro`    |
| 34.   | Vearnl          | `vearnl`      |

## Available Direct-Link Generators

* The following dl-generators (with corresponding types) are supported:

| S.No. | DL Generators   | Type              |
|-------|-----------------|-------------------|
| 1.    | AndroidDataHost | `androiddatahost` |
| 2.    | AnonFiles       | `anonfiles`       |
| 3.    | AntFiles        | `antfiles`        |
| 4.    | ArtStation      | `artstation`      |
| 5.    | Fembed          | `fembed`          |
| 6.    | FilesIm         | `filesIm`         |
| 7.    | Github          | `github`          |
| 8.    | GoFile          | `gofile`          |
| 9.    | HXFile          | `hxfile`          |
| 10.   | KrakenFiles     | `krakenfiles`     |
| 11.   | LetsUpload      | `letsupload`      |
| 12.   | LinkPoi         | `linkpoi`         |
| 13.   | MDisk           | `mdisk`           |
| 14.   | MediaFire       | `mediafire`       |
| 15.   | MegaUP          | `megaup`          |
| 16.   | Mirrored        | `mirrored`        |
| 17.   | OSDN            | `osdn`            |
| 18.   | PandaFile       | `pandafile`       |
| 19.   | PixelDrain      | `pixeldrain`      |
| 20.   | ReUpload        | `reupload`        |
| 21.   | SBEmbed         | `sbembed`         |
| 22.   | SFile           | `sfile`           |
| 23.   | SourceForge     | `sourceforge`     |
| 24.   | StreamLare      | `streamlare`      |
| 25.   | StreamTape      | `streamtape`      |
| 26.   | UserVideo       | `uservideo`       |
| 27.   | WeTransfer      | `wetransfer`      |
| 28.   | Yandex Disk     | `yandex_disk`     |
| 29.   | ZippyShare      | `zippyshare`      |
| 30.   | SolidFiles      | `solidfiles`      |
| 31.   | UploadEE        | `uploadee`        |
| 32.   | Bunkr           | `bunkr_cyber`     |
| 33.   | CyberDrop       | `bunkr_cyber`     |
| 34.   | Pixl            | `pixl`            |
| 35.   | SendCM          | `sendcm`          |
| 36.   | GDBot           | `gdbot`           |
| 37.   | MDisk MPD       | `mdisk_mpd`       |
| 38.   | Dropbox         | `dropbox`         |
| 39.   | MP4Upload       | `mp4upload`       |
| 40.   | StreamSB        | `streamsb`        |
| 41.   | UploadBaz       | `uploadbaz`       |
| 42.   | Uppit           | `uppit`           |
| 43.   | UsersCloud      | `userscloud`      |
| 44.   | MyCloud         | `mycloud`         |
| 45.   | Videovard       | `videovard`       |
| 46.   | Vidstream       | `vidstream`       |

## Available Misc Services

* The following misc services (with corresponding types) are supported:

| S.No. | Misc Service         | Type                   |
|-------|----------------------|------------------------|
| 1.    | Wikipedia Search     | `wiki_search`          |
| 2.    | XDA Search           | `xda_search`           |
| 3.    | Youtube Search       | `youtube_search`       |
| 4.    | XDA Search           | `xda_search`           |
| 5.    | Dictionary Search    | `dictionary_search`    |
| 6.    | Google Search        | `google_search`        |
| 7.    | Github Search        | `github_search`        |
| 8.    | Image Search         | `image_search`         |
| 9.    | Lyrics Search        | `lyrics_search`        |
| 10.   | NPM Search           | `npm_search`           |
| 11.   | Pypi Search          | `pypi_search`          |
| 12.   | Reddit Search        | `reddit_search`        |
| 13.   | Spellchecker         | `spellcheck`           |
| 14.   | TG-Sticker Search    | `tgsticker_search`     |
| 15.   | Stackoverflow Search | `stackoverflow_search` |
| 16.   | Torrent Search       | `torrent_search`       |
| 17.   | TMDB Search          | `tmdb_search`          |
| 18.   | Urban Search         | `urban_search`         |
| 19.   | Unsplash Search      | `unsplash_search`      |
| 20.   | Koo Search           | `koo_search`           |
| 21.   | AnimeChar Search     | `animechar_search`     | 
| 22.   | Winget Search        | `winget_search`        |
| 23.   | OmgUbuntu Search     | `omgubuntu_search`     |

## Available Pasting Services

* The following paste sites (with corresponding types) are supported:

| S.No. | Paste Service |     Type         |
|-------|---------------|------------------|
| 1.    | Telegra.ph    | `telegraph_paste`|
| 2.    | KatBin        | `katbin_paste`   |
| 3.    | NekoBin       | `nekobin_paste`  |
| 4.    | HasteBin      | `hastebin_paste` |
| 5.    | Rentry        | `rentry_paste`   |
| 6.    | Pastingga     | `pastingga_paste`|
| 7.    | PastyLus      | `pastylus_paste` |
| 8.    | SpaceBin      | `spacebin_paste` |

## Available Link Shorteners

* The following shortlink generators/websites (with corresponding types) are supported:

| S.No. | Link-Shorteners |     Type        |
|-------|-----------------|-----------------|
| 1.    | Bit.ly          | `bitly_shorten` |
| 2.    | Da.gd           | `dagd_shorten`  |
| 3.    | Tinyurl.com     | `tinyurl_shorten`|
| 4.    | Osdb.link       | `osdb_shorten`  |
| 5.    | Ttm.sh          | `ttm_shorten`   |
| 6.    | Is.gd           | `isgd_shorten`  |
| 7.    | V.gd            | `vgd_shorten`   |
| 8.    | Click.ru        | `clckru_shorten`|
| 9.    | Chilp.it        | `clilp_shorten` |

## Available Site Scrapers

* The following site scrapers (with corresponding types) are supported:

| S.No. | Site-Scrapers          | Type                 |
|-------|------------------------|----------------------|
| 1.    | AtishMKV Scraper       | `atishmkv_scrap`     |
| 2.    | Bhadoo Index Scraper   | `index_scrap`        |
| 3.    | Cinevez Scraper        | `cinevez_scrap`      |
| 4.    | Cinevood Scraper       | `cinevood_scrap`     |
| 5.    | FileCrypt Scraper      | `filecrypt_scrap`    |
| 6.    | HTPMovies Scraper      | `htpmovies_scrap`    |
| 7.    | IGG Games Scraper      | `igggames_scrape`    |
| 8.    | Moviesdrama Scraper    | `moviesdrama_scrap`  |
| 9.    | Privatemoviez Scraper  |`privatemoviez_scrape`|
| 10.   | Sharespark Scraper     | `sharespark_scrap`   |
| 11.   | Website Magnet Scraper | `magnet_scrap`       |
| 12.   | OlaMovies Scraper      | `olamovies_scrap`    |
| 13.   | Psa.pm Site Scraper    | `psa_scrap`          |
| 14.   | TaeMovies Site Scraper | `taemovies_scrap`    |
| 15.   | TeleguFlix Scraper     | `teleguflix_scrap`   |
| 16.   | Toonworld4all Scraper  | `toonworld4all_scrap`|
| 17.   | AnimeRemux Scraper     | `animeremux_scrap`   |
| 18.   | BenzMovies Scraper     | `benzmovies_scrape`  |
| 19.   | MoviesBoss Scraper     | `moviesboss_scrape`  |
| 20.   | MoviesMod Scraper      | `moviesmod_scrape`   |
| 21.   | SkyMoviesHD Scraper    | `skymovieshd_scrape` |
| 22.   | TamilTVToons Scraper   | `tamiltvtoons_scrape`|
| 23.   | MKVGuru Scraper        | `mkvguru_scrape`     |


## Sample Requests

1. cURL
```sh
curl -H "Content-Type: application/json" -X POST -d '{"type": "adfly", "url": ""}' http://localhost:5000/api/bypass
```
2. Python
```py
import requests

resp = requests.post("https://localhost:500/api/bypass", json={
   "type": "adfly",
   "url": "url"
})
res = resp.json()
if res["success"] is True:
   print(res["url"])
else:
   print(res["msg"])
```
---


# Credits

* Thanks to [Akshett Rai Jindal](https://github.com/akshettrj) for writing the Base Code and Structure of Flask API
* Thanks to [Yukki](https://github.com/xcscxr) for Bypassing Scripts
* Thanks to [Sanjit](https://github.com/sanjit-sinha) for Rocklinks Bypass and Index Scraper
* Thanks to [zevtyardt](https://github.com/zevtyardt/lk21) for LK21 Bypasser
* Thanks to [Disha Patel](https://github.com/dishapatel010) for ArtStation, MDisk and WeTransfer Direct link Gen
* Thanks to [Bipin Krishna](https://github.com/bipinkrish) for OlaMovies, IGG Games and FileCrypt Site Scrapers
* Thanks to [Jack](https://github.com/JohnWickKeanue) for various Bypasses and Scrapers
* Thanks to [Emily](https://github.com/missemily22) for writing the Code and few bypassers