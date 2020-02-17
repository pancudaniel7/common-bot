from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.webdriver import WebDriver


def check_element_exists_by_css(driver: WebDriver, selector: str):
    try:
        driver.find_elements_by_css_selector(selector)
    except NoSuchElementException:
        return False
    return True


def check_element_exists_by_name(driver: WebDriver, name: str):
    try:
        driver.find_element_by_name(name)
    except NoSuchElementException:
        return False
    return True
