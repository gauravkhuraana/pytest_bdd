
import requests

from pytest_bdd import scenarios,given, then, parsers
#Shared Variables
DUCKDUCKGOAPI = 'https://api.duckduckgo.com/'

#Scenarios

scenarios('../feature/duckduckgo.feature', example_converters=dict(phrase=str))

#Given Steps


@given('the DuckDuckGo API is queried with "<phrase>"', target_fixture='ddg_response')
def ddg_response(phrase):
    params = {'q': phrase, 'format': 'json'}
    response = requests.get(DUCKDUCKGOAPI, params=params)
    return response

#then Steps

@then('the response contains results for "<phrase>"')
def ddg_Response_contents(ddg_response, phrase):
    assert  phrase.lower() == ddg_response.json()['Heading'].lower()


@then(parsers.parse('the response status code is "{code:d}"'))
def ddg_response_code(ddg_response, code):
    assert ddg_response.status_code == code

