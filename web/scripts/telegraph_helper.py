import os
from random import SystemRandom
from string import ascii_letters
from time import sleep

from web import LOGGER

from .telegraph.api import Telegraph
from .telegraph.exceptions import RetryAfterError

telegraph_name = os.environ.get("TELEGRAPH_NAME", "EmilyAPI")
telegraph_link = os.environ.get("TELEGRAPH_LINK", "https://github.com/missemily22")


class TelegraphHelper:
    def __init__(self, author_name=None, author_url=None):
        self.api_url = "graph.org"
        self.telegraph = Telegraph()
        self.short_name = "".join(SystemRandom().choices(ascii_letters, k=8))
        self.access_token = None
        self.author_name = author_name
        self.author_url = author_url
        self.create_account()

    def create_account(self):
        self.telegraph.create_account(
            short_name=self.short_name,
            author_name=self.author_name,
            author_url=self.author_url,
        )
        self.access_token = self.telegraph.get_access_token()
        LOGGER.info("Creating Telegraph Account!")

    def create_page(self, title, content):
        try:
            return self.telegraph.create_page(
                title=title,
                author_name=self.author_name,
                author_url=self.author_url,
                html_content=content,
            )
        except RetryAfterError as st:
            LOGGER.warning(
                f"Telegraph Flood control exceeded. I will sleep for {st.retry_after} seconds."
            )
            sleep(st.retry_after)
            return self.create_page(title, content)

    def edit_page(self, path, title, content):
        try:
            return self.telegraph.edit_page(
                path=path,
                title=title,
                author_name=self.author_name,
                author_url=self.author_url,
                html_content=content,
            )
        except RetryAfterError as st:
            LOGGER.warning(
                f"Telegraph Flood control exceeded. I will sleep for {st.retry_after} seconds."
            )
            sleep(st.retry_after)
        return self.edit_page(path, title, content)

    def edit_telegraph(self, path, tele_cont):
        nxt_page = 1
        prev_page = 0
        num_of_path = len(path)
        for content in tele_cont:
            if nxt_page == 1:
                content += (
                    f'<b><a href="https://{self.api_url}/{path[nxt_page]}">Next</a></b>'
                )
                nxt_page += 1
            else:
                if prev_page <= num_of_path:
                    content += f'<b><a href="https://{self.api_url}/{path[prev_page]}">Previous</a></b>'
                    prev_page += 1
                if nxt_page < num_of_path:
                    content += f'<b> | <a href="https://{self.api_url}/{path[nxt_page]}">Next</a></b>'
                    nxt_page += 1
            self.edit_page(path=path[prev_page], title=telegraph_name, content=content)
        return


telegraph = TelegraphHelper(telegraph_name, telegraph_link)
