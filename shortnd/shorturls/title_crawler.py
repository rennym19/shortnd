import requests
from bs4 import BeautifulSoup
from redis import Redis
from rq import Queue
import time

def crawl_title(url_object):
    q = Queue(connection=Redis())
    job = q.enqueue(get_title_from_url, url_object.original_url)
    return job

def get_title_from_url(url_object):
    response = requests.get(url_object.original_url)
    if response.status_code == 200:
        return extract_title_from_html(response.text)
    return None

def extract_title_from_html(html_doc):
    html = BeautifulSoup(html_doc, 'html.parser')
    return html.title.text
