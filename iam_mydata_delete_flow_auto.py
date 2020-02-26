# FILE: iam_mydata_delete_flow_auto.py
# DESC: use Selenium with Python to automate Delete work order creation on E2E
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# ------------------------------------------------------------------------------
#                                  CONSTANTS
# ------------------------------------------------------------------------------
WAIT_TIMEOUT = 20 # seconds
IAM_AUTH_URL_E2E = 'https://accounts-e2e.intuit.com/index.html?iux_v3=true'
TEST_USERNAME = 'iamtestpass_1582737853261' # NOTE: This needs new test user for new request
TEST_USERPASS = 'Intuit01-'

# ------------------------------------------------------------------------------
#                            BROWSER-SPECIFIC WEB DRIVERS
# ------------------------------------------------------------------------------

# FIREFOX - geckodriver
browser = webdriver.Firefox()

# CHROME chromedriver (80)
# options = webdriver.ChromeOptions()
# options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" 
# chrome_driver_binary = "/usr/local/bin/chromedriver"
# browser = webdriver.Chrome(chrome_driver_binary, chrome_options=options)

# ------------------------------------------------------------------------------
#                                UTILITY METHODS
# ------------------------------------------------------------------------------

def wait_for_elem_select(selector):
    return WebDriverWait(browser, WAIT_TIMEOUT).until(lambda browser: browser.find_element_by_css_selector(selector))

# ------------------------------------------------------------------------------
#                                SCRIPT LOGIC
# ------------------------------------------------------------------------------

# Tests Auth Delete Flow (No Products) on E2E
browser.get(IAM_AUTH_URL_E2E)
browser.maximize_window()