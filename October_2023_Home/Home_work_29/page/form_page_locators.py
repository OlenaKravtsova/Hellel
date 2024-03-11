coding: 'utf-8'
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class FieldButtonPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_field = (By.CSS_SELECTOR, ".icon-comfy.header-search-form .header-search-form__input")
        self.submit_button = (By.XPATH, "//span[contains(text(), 'Знайти')]")
        self.url = "https://comfy.ua/ua/"

    def open(self) -> "FieldButtonPage":
        self.driver.get(self.url)
        return self

    def fill_search_field(self, text: str) -> None:
        self.driver.find_element(*self.search_field).send_keys(text)

    def click_submit(self) -> None:
        self.driver.find_element(*self.submit_button).click()

    def get_result_search(self):
        return self.driver.find_element(*self.result_search).text

    def scroll_down(self) -> None:
        self.driver.execute_script("window.scrollBy(0, 500);")

