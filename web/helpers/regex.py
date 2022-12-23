import re

import requests

re_exp = {
    "VIDSTREAM_RE": r"(?P<scheme>https?://)?(?P<host>(?:\S+.)?(?:vidstreamz|vidstream|vizcloud2)\.(?:online|pro))/(?:embed|e)/(?P<id>[A-Z0-9]+)",
    "MCLOUD_RE": r"(?P<scheme>https?://)?(?P<host>(?:\S+.)?mcloud\.to)/(?:embed|e)/(?P<id>[a-zA-Z0-9]+)",
    "VIDEOVARD_RE": r"(?P<scheme>https?://)?(?P<host>(?:\S+.)?videovard\.(?:sx|to))/[ved]/(?P<id>[a-zA-Z0-9]+)",
}


def is_a_url(url: str):
    url = re.match(
        r"((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*",
        url,
    )
    return bool(url)


def url_exists(url) -> bool:
    try:
        with requests.get(url, stream=True) as response:
            try:
                response.raise_for_status()
                return True
            except requests.exceptions.HTTPError:
                return False
    except requests.exceptions.ConnectionError:
        return False


def is_artstation_link(url: str):
    url = re.match(r"artstation\.com/(?:artwork|projects)/([0-9a-zA-Z]+)", url)
    return bool(url)


def is_sendcm_folder_link(url: str):
    return (
        "https://send.cm/s/"
        or "https://send.cm/?sort"
        or "https://send.cm/?sort_field"
        or "https://send.cm/?sort_order"
    ) in url
