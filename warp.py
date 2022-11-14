import urllib.request
import json
import datetime
import random
import string
import time
import os

from web import LOGGER

referrer = os.environ.get("WARP_ID", "1a61d242-54ee-4a55-af1a-1114342b4cf9")

def genString(stringLength):
    try:
        letters = string.ascii_letters + string.digits
        return "".join(random.choice(letters) for i in range(stringLength))
    except Exception as error:
        LOGGER.error(error)

def digitString(stringLength):
    try:
        digit = string.digits
        return "".join((random.choice(digit) for i in range(stringLength)))
    except Exception as error:
        LOGGER.error(error)

url = f"https://api.cloudflareclient.com/v0a{digitString(3)}/reg"
def run():
    try:
        install_id = genString(22)
        body = {"key": "{}=".format(genString(43)),
                "install_id": install_id,
                "fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
                "referrer": referrer,
                "warp_enabled": False,
                "tos": datetime.datetime.now().isoformat()[:-3] + "+02:00",
                "type": "Android",
                "locale": "es_ES"}
        data = json.dumps(body).encode("utf8")
        headers = {"Content-Type": "application/json; charset=UTF-8",
                    "Host": "api.cloudflareclient.com",
                    "Connection": "Keep-Alive",
                    "Accept-Encoding": "gzip",
                    "User-Agent": "okhttp/3.12.1"
                    }
        req = urllib.request.Request(url, data, headers)
        response = urllib.request.urlopen(req)
        status_code = response.getcode()
        return status_code
    except Exception:
        time.sleep(15)
        run()

g = 0
b = 0
limit = 50

while True:
    result = run()
    if result == 200:
        g += 1
        if g > limit:
            LOGGER.info(f"[#] Total: {g} Good {b} Bad")
            limit += 50
        time.sleep(8)
    else:
        b += 1
        time.sleep(8)