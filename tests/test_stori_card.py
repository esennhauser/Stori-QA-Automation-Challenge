from pages.practice_page import PracticePage
import pytest
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


@pytest.fixture(scope="class")
def practice(test_info):
    practice_page = PracticePage(test_info[0], test_info[1])
    return practice_page


class TestStoriCard:

    def test_suggestion_class_example(self, practice):
        print("\n\t\t-----Test writing and selecting 'Mexico'-----\n")
        practice.look_for("Me")
        practice.click_by_xpath(practice.Mexico)
        suggestion_selected = practice.select_element_by_xpath(practice.suggestion_class_textbox).get_attribute('value')
        try:
            assert "Mexico" in suggestion_selected, "ERROR. Mexico not selected. "
            print("Country 'Mexico' selected successfully. \n")
            print("Test Passed.")
        except Exception as ex:
            print("Test Failed.")
            practice.errors.append(ex)

    def test_dropdown_example(self, practice):
        print("\n\t\t-----Test Select Option 2 and 3-----\n")
        dropdown = Select(practice.select_element_by_xpath(practice.dropdown_example))
        practice.select_option_by_xpath(practice.dropdown_example, practice.option_2)
        dropdown_selected_first = dropdown.first_selected_option.text
        practice.select_option_by_xpath(practice.dropdown_example, practice.option_3)
        dropdown_selected_second = dropdown.first_selected_option.text
        try:
            assert "Option2" in dropdown_selected_first, "ERROR. Not verified."
            print("Options 2 selected successfully. ")
        except Exception as ex:
            practice.errors.append(ex)
        try:
            assert "Option3" in dropdown_selected_second, "ERROR. Not verified."
            print("Options 3 selected successfully. \n")
            print("Test Passed.")
        except Exception as ex:
            print("Test Failed.")
            practice.errors.append(ex)

    def test_switch_window_example(self, practice):
        print("\n\t\t-----Test Click and Verify-----\n")
        practice.click_by_xpath(practice.open_window_button)
        emerging_window = WebDriverWait(practice.driver, 10).until(ec.number_of_windows_to_be(2))
        windows = practice.driver.window_handles
        practice.driver.switch_to.window(windows[1])
        expected_message = "30 DAY MONEY BACK GUARANTEE"
        element_expected_in_emerging_window = practice.select_element_by_xpath(practice.element_expected)
        try:
            assert element_expected_in_emerging_window is not None, "ERROR, Element not found."
            try:
                assert expected_message in element_expected_in_emerging_window.text, "ERROR, Test failed. "
                print("30 DAY MONEY BACK GUARANTEE Window opened successfully. ")
                print("Test Passed.")
            except Exception as ex:
                practice.errors.append(ex)
        except Exception as ex:
            print("Test Failed. Element not found.")
            practice.errors.append(ex)
        practice.driver.close()
        practice.driver.switch_to.window(windows[0])

    def test_switch_tab_example(self, practice):
        print("\n\t\t-----Test open tab and verify button.-----\n")
        practice.click_by_css(practice.open_tab)
        windows = practice.driver.window_handles
        practice.driver.switch_to.window(windows[1])
        # The button specified in the exam is not in the page.
        element_expected = practice.select_element_by_xpath(practice.view_all_courses)
        try:
            assert element_expected is not None, "Test Failed. Element not found. "
            button_picture = "open_tab_and_verify_button.png"
            practice.driver.save_screenshot(button_picture)
            print("Test Passed.")
        except Exception as ex:
            print("Test Failed. Element not found.")
            practice.errors.append(ex)
        # Next, I do the same thing asked but with the button 'Access all our courses' which
        # does exist in the page. Is out of scope, I only do it to show.
        element_expected = practice.select_element_by_xpath(practice.access_all_our_courses)
        try:
            assert element_expected is not None, "Test Failed. Element not found. "
            button_picture = "open_tab_and_verify_button.png"
            practice.driver.save_screenshot(button_picture)
        except Exception as ex:
            practice.errors.append(ex)
        practice.driver.switch_to.window(windows[0])
        time.sleep(4)

    def test_switch_to_alert_example(self, practice):
        print("\n\t\t-----Test alert button-----\n")
        practice.introduce_text_by_xpath(practice.switch_to_alert_textbox, "Stori Card")
        practice.click_by_css(practice.alert_button)
        alert = WebDriverWait(practice.driver, 10).until(ec.alert_is_present())
        print(alert.text)
        alert.accept()
        print("Test Passed.")

    def test_switch_to_confirm_example(self, practice):
        print("\n\t\t-----Test confirm button-----\n")
        practice.introduce_text_by_xpath(practice.switch_to_alert_textbox, "Stori Card")
        practice.click_by_xpath(practice.confirm_button)
        WebDriverWait(practice.driver, 10).until(ec.alert_is_present())
        alert = practice.driver.switch_to.alert
        try:
            assert alert.text == "Hello Stori Card, Are you sure you want to confirm?", "ERROR. Test failed. "
            print("Messagge as expected: " + alert.text)
            alert.accept()
            print("Test Passed.")
        except Exception as ex:
            print("Test failed.")
            practice.errors.append(ex)

    def test_web_table_example(self, practice):
        print("\n\t\t-----Test courses that are $25.-----\n")
        rows = list(range(2, 12))
        n = 0
        courses = []
        for row in rows:
            price = practice.take_value(row, practice.price_column).text
            course_name = practice.take_value(row, practice.course_column).text
            if price == "25":
                n += 1
                courses.append(course_name)
        print("The number of courses that are $25 is: " + str(n))
        print("The courses are the following: \n")
        for c in courses:
            print(c)
        print("Test Passed.")

    def test_web_table_fixed_header(self, practice):
        print("\n\t\t-----Test names of all the Engineers-----\n")
        rows = list(range(1, 10))
        for row in rows:
            position = practice.take_value(row, practice.position_column).text
            name = practice.take_value(row, practice.name_column).text
            if position == "Engineer":
                print(name + " is an engineer. ")
        print("Test Passed.")

    def test_iframe_example(self, practice):
        print("\n\t\t-----Test get the text highlighted in blue.-----\n")
        iframe = practice.driver.find_element(By.CSS_SELECTOR, "#courses-iframe")
        practice.driver.switch_to.frame(iframe)
        element_paragraph_requested = practice.select_element_by_xpath(practice.highlighted_paragraph)
        paragraph_requested = element_paragraph_requested.text
        print(paragraph_requested)
        words = paragraph_requested.split()
        for index, word in enumerate(words):
            if index % 2 != 0:
                print(word)
        print("Test Passed.")

