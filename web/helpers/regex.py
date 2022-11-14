import re


def is_a_url(url: str):
    url = re.match(
        r"((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*",
        url,
    )
    return bool(url)


def is_artstation_link(url: str):
    url = re.match(r"artstation\.com/(?:artwork|projects)/([0-9a-zA-Z]+)", url)
    return bool(url)


def is_sendcm_folder_link(url: str):
    return (
        "https://send.cm/s/" in url
        or "https://send.cm/?sort" in url
        or "https://send.cm/?sort_field" in url
        or "https://send.cm/?sort_order" in url
    )
