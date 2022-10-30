import json
import logging
import os

from flask import jsonify, request
from flask_restful import Resource
from waitress import serve

from web import (BYP_SUP_SITES, DIRT_SUP_SITES, MISC_SUP_SITES,
                 PASTE_SUP_SITES, SCRAPE_SUP_SITES, SHRT_SUP_SITES, abc, app)

logging.basicConfig(
    format="%(asctime)s - [%(filename)s:%(lineno)d] - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("flask").setLevel(logging.WARNING)
logging.getLogger("flask_restful").setLevel(logging.WARNING)


class Greeting(Resource):
    def get(self):
        return "Emily`s API is Up & Running!"


class Depriciated(Resource):
    def get(self):
        return "This EndPoint is not valid anymore!"


abc.add_resource(Greeting, "/")
abc.add_resource(Depriciated, "/api")


@app.route("/api/bypass", methods=["GET", "POST"])
def json_api():
    data = request.data.strip()
    if len(data) == 0:
        return jsonify({"success": False, "msg": "No Data Provided"})
    try:
        data = json.loads(data)
    except json.JSONDecodeError as ex:
        LOGGER.error(f"Could not parse the data as JSON: {ex}")
        return jsonify(
            {"success": False, "msg": f"Could not parse the data as JSON: {ex}"}
        )
    data_keys = data.keys()
    if len(data_keys) != 2 or "type" not in data_keys or "url" not in data_keys:
        LOGGER.error("Parameters Incorrect!")
        return jsonify({"success": False, "msg": "Parameters Incorrect!"})
    byp_type = data["type"]
    usr_link = data["url"]
    LOGGER.info(f"Received URL - {byp_type} - {usr_link}")
    if byp_type not in BYP_SUP_SITES.keys():
        LOGGER.error("Site Not Supported!")
        return jsonify({"success": False, "msg": "Site Not Supported!"})
    byp_func = BYP_SUP_SITES[byp_type]
    try:
        result = byp_func(usr_link)
        LOGGER.info(f"Successfully Bypassed - {byp_type} - {result}")
        return jsonify(
            {"success": True, "url": result, "credits": "Made by Miss Emily", "type": byp_type}
        )
    except Exception as ex:
        LOGGER.error(f"Failed to Perform Action due to : {ex}!")
        return jsonify(
            {"success": False, "msg": f"Failed to Perform Action due to : {ex}"}
        )


@app.route("/api/direct", methods=["GET", "POST"])
def json_api_2():
    data = request.data.strip()
    if len(data) == 0:
        return jsonify({"success": False, "msg": "No Data Provided"})
    try:
        data = json.loads(data)
    except json.JSONDecodeError as ex:
        LOGGER.error(f"Could not parse the data as JSON: {ex}")
        return jsonify(
            {"success": False, "msg": f"Could not parse the data as JSON: {ex}"}
        )
    data_keys = data.keys()
    if len(data_keys) != 2 or "type" not in data_keys or "url" not in data_keys:
        LOGGER.error("Parameters Incorrect!")
        return jsonify({"success": False, "msg": "Parameters Incorrect!"})
    dir_type = data["type"]
    usr_link = data["url"]
    LOGGER.info(f"Received URL - {dir_type} - {usr_link}")
    if dir_type not in DIRT_SUP_SITES.keys():
        LOGGER.error("Site Not Supported!")
        return jsonify({"success": False, "msg": "Site Not Supported!"})
    dir_func = DIRT_SUP_SITES[dir_type]
    try:
        result = dir_func(usr_link)
        LOGGER.info(f"Successfully Generator DL - {dir_type} - {result}")
        return jsonify(
            {"success": True, "url": result, "credits": "Made by Miss Emily", "type": dir_type}
        )
    except Exception as ex:
        LOGGER.error(f"Failed to Perform Action due to : {ex}!")
        return jsonify(
            {"success": False, "msg": f"Failed to Perform Action due to : {ex}"}
        )


@app.route("/api/misc", methods=["GET", "POST"])
def json_api_3():
    data = request.data.strip()
    if len(data) == 0:
        return jsonify({"success": False, "msg": "No Data Provided"})
    try:
        data = json.loads(data)
    except json.JSONDecodeError as ex:
        LOGGER.error(f"Could not parse the data as JSON: {ex}")
        return jsonify(
            {"success": False, "msg": f"Could not parse the data as JSON: {ex}"}
        )
    data_keys = data.keys()
    if len(data_keys) != 2 or "type" not in data_keys or "query" not in data_keys:
        LOGGER.error("Parameters Incorrect!")
        return jsonify({"success": False, "msg": "Parameters Incorrect!"})
    misc_type = data["type"]
    usr_query = data["query"]
    LOGGER.info(f"Received URL - {misc_type} - {usr_query}")
    if misc_type not in MISC_SUP_SITES.keys():
        LOGGER.error("Site Not Supported!")
        return jsonify({"success": False, "msg": "Site Not Supported!"})
    misc_func = MISC_SUP_SITES[misc_type]
    try:
        result = misc_func(usr_query)
        LOGGER.info(f"Successfully Performed Misc Service - {misc_type} - {result}")
        return jsonify(
            {"success": True, "url": result, "credits": "Made by Miss Emily", "type": misc_type}
        )
    except Exception as ex:
        LOGGER.error(f"Failed to Perform Action due to : {ex}!")
        return jsonify(
            {"success": False, "msg": f"Failed to Perform Action due to : {ex}"}
        )


@app.route("/api/paste", methods=["GET", "POST"])
def json_api_4():
    data = request.data.strip()
    if len(data) == 0:
        return jsonify({"success": False, "msg": "No Data Provided"})
    try:
        data = json.loads(data)
    except json.JSONDecodeError as ex:
        LOGGER.error(f"Could not parse the data as JSON: {ex}")
        return jsonify(
            {"success": False, "msg": f"Could not parse the data as JSON: {ex}"}
        )
    data_keys = data.keys()
    if len(data_keys) != 2 or "type" not in data_keys or "text" not in data_keys:
        LOGGER.error("Parameters Incorrect!")
        return jsonify({"success": False, "msg": "Parameters Incorrect!"})
    paste_type = data["type"]
    usr_text = data["text"]
    LOGGER.info(f"Received URL - {paste_type} - {usr_text}")
    if paste_type not in PASTE_SUP_SITES.keys():
        LOGGER.error("Site Not Supported!")
        return jsonify({"success": False, "msg": "Site Not Supported!"})
    paste_func = PASTE_SUP_SITES[paste_type]
    try:
        result = paste_func(usr_text)
        LOGGER.info(f"Successfully Pasted - {paste_type} - {result}")
        return jsonify(
            {"success": True, "url": result, "credits": "Made by Miss Emily", "type": paste_type}
        )
    except Exception as ex:
        LOGGER.error(f"Failed to Perform Action due to : {ex}!")
        return jsonify(
            {"success": False, "msg": f"Failed to Perform Action due to : {ex}"}
        )


@app.route("/api/scraper", methods=["GET", "POST"])
def json_api_5():
    data = request.data.strip()
    if len(data) == 0:
        return jsonify({"success": False, "msg": "No Data Provided"})
    try:
        data = json.loads(data)
    except json.JSONDecodeError as ex:
        LOGGER.error(f"Could not parse the data as JSON: {ex}")
        return jsonify(
            {"success": False, "msg": f"Could not parse the data as JSON: {ex}"}
        )
    data_keys = data.keys()
    if len(data_keys) != 2 or "type" not in data_keys or "url" not in data_keys:
        LOGGER.error("Parameters Incorrect!")
        return jsonify({"success": False, "msg": "Parameters Incorrect!"})
    scrap_type = data["type"]
    usr_link = data["url"]
    LOGGER.info(f"Received URL - {scrap_type} - {usr_link}")
    if scrap_type not in SCRAPE_SUP_SITES.keys():
        LOGGER.error("Site Not Supported!")
        return jsonify({"success": False, "msg": "Site Not Supported!"})
    scrap_func = SCRAPE_SUP_SITES[scrap_type]
    try:
        result = scrap_func(usr_link)
        LOGGER.info(f"Successfully Scraped - {scrap_type} - {result}")
        return jsonify(
            {"success": True, "url": result, "credits": "Made by Miss Emily", "type": scrap_type}
        )
    except Exception as ex:
        LOGGER.error(f"Failed to Perform Action due to : {ex}!")
        return jsonify(
            {"success": False, "msg": f"Failed to Perform Action due to : {ex}"}
        )


@app.route("/api/shorten", methods=["GET", "POST"])
def json_api_6():
    data = request.data.strip()
    if len(data) == 0:
        return jsonify({"success": False, "msg": "No Data Provided"})
    try:
        data = json.loads(data)
    except json.JSONDecodeError as ex:
        LOGGER.error(f"Could not parse the data as JSON: {ex}")
        return jsonify(
            {"success": False, "msg": f"Could not parse the data as JSON: {ex}"}
        )
    data_keys = data.keys()
    if len(data_keys) != 2 or "type" not in data_keys or "url" not in data_keys:
        LOGGER.error("Parameters Incorrect!")
        return jsonify({"success": False, "msg": "Parameters Incorrect!"})
    shrtn_type = data["type"]
    usr_link = data["url"]
    LOGGER.info(f"Received URL - {shrtn_type} - {usr_link}")
    if shrtn_type not in SHRT_SUP_SITES.keys():
        LOGGER.error("Site Not Supported!")
        return jsonify({"success": False, "msg": "Site Not Supported!"})
    shrtn_func = SHRT_SUP_SITES[shrtn_type]
    try:
        result = shrtn_func(usr_link)
        LOGGER.info(f"Successfully Shortened - {shrtn_type} - {result}")
        return jsonify(
            {"success": True, "url": result, "credits": "Made by Miss Emily", "type": shrtn_type}
        )
    except Exception as ex:
        LOGGER.error(f"Failed to Perform Action due to : {ex}!")
        return jsonify(
            {"success": False, "msg": f"Failed to Perform Action due to : {ex}"}
        )


serve(app, host="0.0.0.0", port=os.environ.get("PORT", 8080))
