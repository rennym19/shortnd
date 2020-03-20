from aloe import before, step, world
from aloe.tools import guess_types
from aloe_django.steps.models import reset_sequence, get_model
from nose.tools import assert_count_equal, assert_dict_equal
from rest_framework.test import APIClient

from ..models import URL

# The steps defined here are used in all features


@before.each_feature
def set_up(feature):
    world.client = APIClient()


@step('I empty the "([^"]+)" table')
def empty_table(self, model_name):
    model_class = get_model(model_name)
    model_class.objects.all().delete()
    reset_sequence(model_class)


@step('I see the following response data')
def check_response_data(self):
    response = world.response.json()
    if isinstance(response, list):
        assert_count_equal(guess_types(self.hashes), response)
    else:
        assert_dict_equal(guess_types(self.hashes)[0], response)


@step('I create the following URLs')
def create_urls(self):
    url_hashes = guess_types(self.hashes)
    
    if url_hashes:
        has_visit_count = True if 'visit_count' in url_hashes[0] else False
    
    for url_hash in guess_types(self.hashes):
        url = URL(original_url=url_hash['original_url'],
                  key=url_hash['key'],
                  title=url_hash['title'],
                  visit_count=url_hash['visit_count'] if has_visit_count else 0)
        url = url.save()
