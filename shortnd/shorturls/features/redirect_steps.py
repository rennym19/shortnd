from aloe import step, world
from nose.tools import assert_true, assert_count_equal, assert_dict_equal
from django.urls import reverse
from rest_framework import status

from . import set_up, empty_table, check_response_data, create_urls


@step('I Click on a shortened url with key "([^"]+)"')
def redirect_to(self, key):
    world.client.get(reverse('shortnd:redirect', args=(key)))


@step('I get redirected to an URL')
def confirm_redirected(self):
    assert_true(world.response.status_code == status.HTTP_302_FOUND)
