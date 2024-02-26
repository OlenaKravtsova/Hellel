from selenium.webdriver.common.by import By

from Hellel.October_23.lesson_25.RadioButtonPage import RadioButton


def test_radio(chrome):
    chrome.get("https://demoqa.com/radio-button")
    ra_yes = RadioButton(driver=chrome, locator=(By.XPATH, "//label[.='{}']//ancestor::div[contains(@class, 'radio')]"), name="Impressive")
    ra_yes.select()
    pass