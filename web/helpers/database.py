import datetime

from pymongo import MongoClient
from pymongo.errors import PyMongoError

from web import DATABASE_URL, LOGGER


class DBHelper:
    def __init__(self):
        self.__err = False
        self.__client = None
        self.__db = None
        self.__col = None
        self.__connect()

    def __connect(self):
        try:
            self.__client = MongoClient(DATABASE_URL)
            self.__db = self.__client["EmilyAPI"]
            self.__col = self.__db["urls"]
            self.__err = False
        except PyMongoError as e:
            LOGGER.error(f"Error in DB connection: {e}")
            self.__err = True

    def new_dblink(self, url, result):
        return dict(
            usr_url=url,
            result_url=result,
            url_added_on=datetime.date.today().isoformat(),
            last_fetched_on=datetime.date.today().isoformat(),
        )

    async def check_dblink(self, url):
        if self.__err:
            return
        usr_url = self.__col.find_one({"usr_url": url})
        if usr_url is not None:
            return usr_url
        self.__client.close()

    async def add_new_dblink(self, url, result):
        if self.__err:
            return
        dblink = self.new_dblink(url, result)
        self.__col.update_one(
            {"usr_url": dblink["usr_url"]},
            {
                "$set": {
                    "result_url": dblink["result_url"],
                    "url_added_on": dblink["url_added_on"],
                    "last_fetched_on": dblink["last_fetched_on"],
                }
            },
            upsert=True,
        )
        self.__client.close()

    async def is_dblink_exist(self, url):
        if self.__err:
            return
        user = await self.check_dblink(url)
        return True if user else False

    async def fetch_dblink_result(self, url):
        if self.__err:
            return
        dblink = await self.check_dblink(url)
        return dblink.get("result_url")

    async def fetch_dblink_added(self, url):
        if self.__err:
            return
        dblink = await self.check_dblink(url)
        return dblink.get("url_added_on")

    async def update_last_fetched_on(self, url):
        if self.__err:
            return
        self.__col.update_one(
            {"usr_url": url},
            {"$set": {"last_fetched_on": datetime.date.today().isoformat()}},
            upsert=True,
        )
        self.__client.close()

    async def get_url_added_on(self, url):
        if self.__err:
            return
        dblink = await self.check_dblink(url)
        return dblink.get("url_added_on")

    async def get_last_fetched_on(self, url):
        if self.__err:
            return
        dblink = await self.check_dblink(url)
        return dblink.get("last_fetched_on")

    async def total_dblinks_count(self):
        if self.__err:
            return
        count = self.__col.count_documents({})
        self.__client.close()
        return count

    def check_db_connection(self):
        if self.__err:
            return
        if not self.__err:
            LOGGER.info("Successfully Connected to DB!")
        self.__client.close()


if DATABASE_URL is not None:
    DBHelper().check_db_connection()
