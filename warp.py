import urllib.request
import json
import datetime
import random
import string
import time
import os
import sys

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
    except Exception as error:
        LOGGER.error("")
        LOGGER.error("[×] Error:", error)

g = 0
b = 0
while True:
    #os.system("cls" if os.name == "nt" else "clear")
    """animation = ["[■□□□□□□□□□] 10%","[■■□□□□□□□□] 20%", "[■■■□□□□□□□] 30%", "[■■■■□□□□□□] 40%", "[■■■■■□□□□□] 50%", "[■■■■■■□□□□] 60%", "[■■■■■■■□□□] 70%", "[■■■■■■■■□□] 80%", "[■■■■■■■■■□] 90%", "[■■■■■■■■■■] 100%"] 
    for i in range(len(animation)):
        time.sleep(0.2)
        sys.stdout.write("\r[∆] Progress: " + animation[i % len(animation)])
        sys.stdout.flush() """
    result = run()
    if result == 200:
        g += 1
        #LOGGER.info(f"\n[•] WARP+ ID: {referrer}")
        LOGGER.info(f"[✓] Added: {g} GB")
        LOGGER.info(f"[#] Total: {g} Good {b} Bad")
        for i in range(20,-1,-1):
            sys.stdout.write(f" Cooldown: {i} seconds")
            sys.stdout.flush()
            time.sleep(8)
    else:
        b += 1
        LOGGER.info(f"[#] Total: {g} Good {b} Bad")
        for i in range(10,-1,-1):
            sys.stdout.write(f" Cooldown: {i} seconds")
            sys.stdout.flush()
            time.sleep(8)