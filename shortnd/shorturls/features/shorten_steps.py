from aloe import step, world
from nose.tools import assert_true, assert_count_equal, assert_dict_equal
from django.urls import reverse

from . import set_up, empty_table, check_response_data, create_urls


@step('I Set the "([^"]+)" in the request body')
def set_url_request_body(self, url):
    world.request_body = {'url': url}


@step('I Send a POST request to the endpoint /shorten/')
def send_shorten_post_request(self):
    world.response = world.client.post(reverse('shortnd:shorten'), world.request_body)
