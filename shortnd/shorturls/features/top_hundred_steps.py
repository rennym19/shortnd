from aloe import step, world
from nose.tools import assert_true, assert_count_equal, assert_dict_equal
from django.urls import reverse

from . import set_up, empty_table, check_response_data, create_urls


@step('I send a GET request to the endpoint /top_hundred/')
def send_shorten_post_request(self):
    world.response = world.client.get(reverse('shortnd:top_hundred'))
