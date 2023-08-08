from pytest_bdd import *
from pages.practice_page import PracticePage
import pytest


@scenario('../suggestion_class.feature', 'look for and select mexico')
def test_suggestion_class():
    pass


@pytest.fixture
@given("we launch browser and go to Automation Practice page")
def setup_function(test_info):
    practice_page = PracticePage(test_info[0], test_info[1])
    return practice_page


@when("we enter the word 'Me'")
def look_for(setup_function):
    print("\n\t\t-----Writing and selecting 'Mexico'-----")
    setup_function.look_for("Me")


@then("we select 'Mexico'")
def select_mexico(setup_function):
    setup_function.click_by_xpath(setup_function.Mexico)
