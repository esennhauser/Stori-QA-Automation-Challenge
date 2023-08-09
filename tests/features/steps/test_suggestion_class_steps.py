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
    print("\n\t\t-----Test writing and selecting 'Mexico' (using pytest-bdd)-----\n")
    setup_function.look_for("Me")


@when("we select 'Mexico'")
def select_mexico(setup_function):
    setup_function.click_by_xpath(setup_function.Mexico)


@then("we can see 'Mexico' is selected")
def verify_mexico(setup_function):
    suggestion_selected = setup_function.select_element_by_xpath(setup_function.suggestion_class_textbox).get_attribute('value')
    try:
        assert "Mexico" in suggestion_selected, "ERROR. Mexico not selected. "
        print("Country 'Mexico' selected successfully. \n")
        print("Test Passed.")
    except Exception as ex:
        print("Test Failed.")
        setup_function.errors.append(ex)
