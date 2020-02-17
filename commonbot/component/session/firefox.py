from selenium import webdriver


def new_session(log_level, firefox_headless):
    options = webdriver.FirefoxOptions()
    options.log.level = log_level

    if firefox_headless.lower() == 'true': options.add_argument('--headless')

    return webdriver.Firefox(options=options)
