import requests
from bs4 import BeautifulSoup
from redis import Redis
from rq import Queue
import time


class TitleCrawler:
    def __init__(self, url_object):
        self.url_object = url_object

    def crawl_title(self):
        q = Queue(connection=Redis())
        job = q.enqueue(self._get_title_from_url)

        # wait a maximum of 10 secs
        elapsed_time = 0
        while elapsed_time < 10 and job.result is None:
            time.sleep(2)
            elapsed_time += 2
        
        if elapsed_time >= 10:
            raise Exception("Timeout")

        self.url_object.title = job.result
        self.url_object.save()

    def _get_title_from_url(self):
        response = requests.get(self.url_object.original_url)
        if response.status_code == 200:
            return self._extract_title_from_html(response.text)
        return None

    def _extract_title_from_html(self, html_doc):
        html = BeautifulSoup(html_doc, 'html.parser')
        return html.title.text
