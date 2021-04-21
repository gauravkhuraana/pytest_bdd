from functools import partial

import pytest
from pytest_bdd import scenarios,parsers, given, when, then

from Cucumbers import CucumberBasket


#@scenario('../feature/cucumber.feature', "Add Cucumbers to a basket")

EXTRA_TYPES = {
    'Number': int,
}

CONVERTOR={
    'initial': int,
    'some': int,
    'total': int,
}
scenarios('../feature/cucumber.feature', example_converters=CONVERTOR)
parse_num = partial(parsers.cfparse, extra_types=EXTRA_TYPES)

#def test_add():
#    pass

@pytest.fixture
@given(parse_num('the basket has "{initial:Number}" cucumbers'))
@given('the basket has "<initial>" cucumbers')
def basket(initial):
    return CucumberBasket(initial_count=initial)

@when(parsers.cfparse('"{some:Number}" cucumbers are added to the basket',EXTRA_TYPES))
@when('"<some>" cucumbers are added to the basket')
def add_cucumbers(basket, some):
    basket.add(some)

@when(parse_num('"{some:Number}" cucumbers are removed from the basket'))
def remove_cucumbers(basket, some):
    basket.remove(some)


@then(parsers.cfparse('the basket contains "{total:Number}" cucumbers',extra_types=dict(Number=int)))
@then('the basket contains "<total>" cucumbers')
def basket_has_total(basket, total):
    assert basket.count == total
