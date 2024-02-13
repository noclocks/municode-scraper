import time
import os

import pandas as pd

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

import re
import requests

def get_towns_by_state(state: str, driver: webdriver.Chrome):
    """
    Get a list of towns by state from municode.com

    Args:
    state (str): the state to get towns from
    driver (webdriver.Chrome): the webdriver to use

    Returns:
    data_out (pd.DataFrame): a dataframe of towns by state
    """

    # assert that the driver is a webdriver.Chrome
    assert isinstance(driver, webdriver.Chrome)
    driver.refresh()

    url = f"https://library.municode.com/{state}"

    xpath_init = '/html/body/div[1]/div[2]/ui-view/div[2]/section/div/div'

    driver.get(url)

    data = driver.find_elements(by=By.XPATH, value=xpath_init)

    time.sleep(2)

    html = data[0].get_attribute("outerHTML")

    url_str = url + '/[\w\.-]+'

    r1 = re.findall(url_str,html)

    towns_list = pd.DataFrame(r1)
    towns_list = towns_list.drop_duplicates().reset_index(drop=True)
    towns_list = towns_list.rename(columns={0: 'url'})

    # add state column (uppercase)
    towns_list['state'] = state.upper()

    # add town column
    towns_list['town'] = towns_list['url'].str.split('/').str[-1]

    # re-order columns
    data_out = towns_list[['state', 'town', 'url']]

    # save to csv
    csv_filename = f'{state}_town_urls.csv'
    data_out.to_csv(csv_filename, index=False)

    # driver.quit()

    return data_out


def identify_tbl(url: str, driver: webdriver.Chrome):

    driver.get(url)

    time.sleep(2)

    xpath_init = '/html/body/div[1]/div[2]/ui-view/mcc-codes/div[2]/section[1]/div[2]'

    data = driver.find_elements(by=By.XPATH, value=xpath_init)

    time.sleep(2)

    html = data[0].get_attribute("outerHTML")

    r2 = re.findall(r'(https?://[^\s]+)', html)

    url = r2[-1]
    url = url[:-1]

    return url

driver = webdriver.Chrome()

town_urls_tbl = get_towns_by_state('ga', driver)

town_urls = town_urls_tbl['url'].tolist()

identify_tbl(town_urls[0], driver)

# DEPRECATIONS

# chrome_options = Options()

# determine if local or docker
# if os.getenv('DOCKER'):
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-dev-shm-usage')
    # chrome_options.binary_location = '/usr/bin/google-chrome'
    # chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-dev-shm-usage')
# elif os.getenv('LOCAL') == 'True':
# chrome_options.add_experimental_option("detach", True)

# chrome_service = ChromeService(ChromeDriverManager().install())
# chrome_service = ChromeService('/usr/bin/chromedriver')
