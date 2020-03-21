import requests
import django_rq
from bs4 import BeautifulSoup

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    'From': 'https://www.google.com'
}

def fetch_title(url):
    django_rq.enqueue(crawl_title, url)

def crawl_title(url_object):
    url_object.title = get_title_from_url(url_object)
    url_object.save()
    return url_object.title

def get_title_from_url(url_object):
    try:
        response = requests.get(url_object.original_url, headers=HEADERS)
        if response.status_code == 200:
            return extract_title_from_html(response.text)
    except Exception:
        return None
    return None

def extract_title_from_html(html_doc):
    html = BeautifulSoup(html_doc, 'html.parser')
    return html.title.text
