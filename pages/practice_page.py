import time
from pages.base_page import BasePage


class PracticePage(BasePage):

    suggestion_class_textbox = "//input[contains(@placeholder,'Type to Select Countries')]"
    Mexico = "//div[@tabindex='-1'][contains(.,'Mexico')]"

    dropdown_example = "//body[1]/div[1]/div[3]/fieldset[1]/select[1]"
    option_1 = "//body[1]/div[1]/div[3]/fieldset[1]/select[1]/option[2]"
    option_2 = "//body[1]/div[1]/div[3]/fieldset[1]/select[1]/option[3]"
    option_3 = "//body[1]/div[1]/div[3]/fieldset[1]/select[1]/option[4]"

    open_window_button = "//button[contains(.,'Open Window')]"
    element_expected = "//*[contains(text(), '30 DAY MONEY BACK GUARANTEE')]"

    open_tab = "//a[contains(@id,'opentab')]"
    view_all_courses = "//a[contains(.,'View all courses')]"
    access_all_our_courses = "//a[contains(.,'Access all our Courses')]"

    switch_to_alert_textbox = "//input[@id='name']"
    alert_button = "//input[@id='alertbtn']"
    confirm_button = "//input[@id='confirmbtn']"

    price_column = "div.block.large-row-spacer:nth-child(5) div.left-align fieldset:nth-child(1) " \
                   "table.table-display:nth-child(2) tbody:nth-child(1) tr:nth-child({}) > td:nth-child(3)"
    course_column = "div.block.large-row-spacer:nth-child(5) div.left-align fieldset:nth-child(1) " \
                    "table.table-display:nth-child(2) tbody:nth-child(1) tr:nth-child({}) > td:nth-child(2)"

    position_column = "div.block.large-row-spacer:nth-child(5) div.right-align div.tableFixHead:nth-child(2)" \
                      " table:nth-child(1) tbody:nth-child(2) tr:nth-child({}) > td:nth-child(2)"
    name_column = "div.block.large-row-spacer:nth-child(5) div.right-align div.tableFixHead:nth-child(2)" \
                  " table:nth-child(1) tbody:nth-child(2) tr:nth-child({}) > td:nth-child(1)"

    highlighted_paragraph = "//li[contains(text(),'His mentorship program is most after in the softwa')]"

    def look_for(self, text):
        try:
            self.click_by_xpath(self.suggestion_class_textbox)
            self.introduce_text_by_xpath(self.suggestion_class_textbox, text)
            time.sleep(2)
        except Exception as ex:
            self.errors.append(ex)

    def take_screenshot_of_button(self, button):
        element_expected = self.select_element_by_xpath(button)
        try:
            assert element_expected is not None, "ERROR, Test failed. "
            button_picture = "screenshot.png"
            self.driver.save_screenshot(button_picture)
        except Exception as ex:
            print("ERROR, Test failed. ")
            self.errors.append(ex)

    def take_screenshot_of_page(self):
        picture = "screenshot2.png"
        self.driver.save_screenshot(picture)

    def take_value(self, row, column):
        price = self.select_element_by_css(column.format(row))
        return price
