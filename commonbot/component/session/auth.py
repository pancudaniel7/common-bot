import logging
import time

from commonbot.component.action import wrapper
from commonbot.component.collector import page_loader
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.phantomjs.webdriver import WebDriver
from selenium.webdriver.remote.remote_connection import LOGGER

from commonbot.component.session import vault


def login(driver: WebDriver, login_url: str, username: str, password: str):
    driver.get(login_url)

    LOGGER.setLevel(logging.INFO)

    page_loader.get_page_source_until_all_names(driver=driver, name='accept_all_cookies')

    elem = driver.find_element_by_name('accept_all_cookies')
    wrapper.function_call_delay(elem.click)

    elem = driver.find_element_by_name('username')
    elem.clear()
    elem.send_keys(username)

    time.sleep(1)

    elem = driver.find_element_by_name('password')
    elem.clear()
    elem.send_keys(password)

    time.sleep(1)
    elem.send_keys(Keys.RETURN)

    time.sleep(1)

    LOGGER.setLevel(logging.DEBUG)


def login_with_vault(driver: WebDriver, login_url: str, vault_address: str, vault_token: str, vault_path: str):
    secrets = vault.get_secrets(vault_address, vault_token, vault_path)
    login(driver, login_url, secrets['data']['username'], secrets['data']['password'])
