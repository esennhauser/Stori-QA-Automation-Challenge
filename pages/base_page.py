from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    errors = []
    driver = None

    def __init__(self, driver, errors):
        self.driver = driver
        self.errors = errors

    def go_to(self, url):
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            print("Page opened: "+str(url))
        except Exception as ex:
            self.errors.append(ex.msg)

    def introduce_text_by_xpath(self, selector, text):
        try:
            val = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.XPATH, selector)))
            val = self.driver.find_element(By.XPATH, selector)
            val.clear()
            val.send_keys(text)
            print("Writing the text: {} ".format(text))
        except Exception as ex:
            self.errors.append(ex.msg)

    def click_by_id(self, selector):
        try:
            val = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.ID, selector)))
            self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.ID, selector)
            val.click()
        except Exception as ex:
            self.errors.append(ex.msg)

    def click_by_xpath(self, selector):
        try:
            WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.XPATH, selector)))
            val = self.driver.find_element(By.XPATH, selector)
            val.click()
        except Exception as ex:
            self.errors.append(ex.msg)

    def click_by_css(self, selector):
        try:
            WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
            val = self.driver.find_element(By.CSS_SELECTOR, selector)
            val.click()
        except Exception as ex:
            self.errors.append(ex.msg)

    def select_element_by_xpath(self, element):
        try:
            val = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.XPATH, element)))
            self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.XPATH, element)
            return val
        except Exception as ex:
            self.errors.append(ex.msg)

    def select_element_by_css(self, element):
        try:
            val = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, element)))
            self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.CSS_SELECTOR, element)
            return val
        except Exception as ex:
            self.errors.append(ex.msg)

    def select_option_by_xpath(self, element, option):
        try:
            val = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.XPATH, element)))
            self.driver.execute_script("arguments[0].scrollIntoView();", val)
            self.click_by_xpath(element)
            self.driver.find_element(By.XPATH, option)
            self.click_by_xpath(option)
        except Exception as ex:
            self.errors.append(ex.msg)