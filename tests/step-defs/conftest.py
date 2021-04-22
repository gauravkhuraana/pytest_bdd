import pytest
import  time
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium import webdriver

#contants
DUCKDUCKGO_HOME = 'https://duckduckgo.com/'


@pytest.fixture
def browser():
    b=webdriver.Firefox()
    b.implicitly_wait(10)
    yield b
    b.quit()

#shared given steps
@given('the DuckDuckGo home page is displayed')
def ddg_home(browser):
    browser.get(DUCKDUCKGO_HOME)