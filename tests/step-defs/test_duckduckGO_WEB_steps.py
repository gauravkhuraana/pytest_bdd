import pytest
import  time
from pytest_bdd import scenarios, given, when, then, parsers

from selenium.webdriver.common.keys import Keys


scenarios('../feature/duckduckgoWebUI.feature')

#Given Steps



@when(parsers.parse('the user searches for "{text}"'))
@when(parsers.parse('the user searches for the phrase:\n{text}'))
def search_phrase(browser, text):
    search_input = browser.find_element_by_name('q')
    search_input.send_keys(text+Keys.RETURN)
   # time.sleep(5)

@then(parsers.parse('one of the results contains "{phrase}"'))
def results_have_one(browser, phrase):
    xpath = "//div[@id='links']//*[contains(text(), '%s')]" % phrase
    results = browser.find_elements_by_xpath(xpath)
    #time.sleep(5)
    assert len(results) > 0

@then(parsers.parse('the results are shown for "{phrase}"'))
def search_results(browser, phrase):
    links_div = browser.find_element_by_id('links')
    assert len(links_div.find_elements_by_xpath('//div')) > 0
    #time.sleep(5)
    search_input = browser.find_element_by_name('q')
    assert search_input.get_attribute('value') == phrase