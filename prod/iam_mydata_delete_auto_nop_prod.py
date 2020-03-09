# FILE: iam_mydata_delete_auto_nop_prod.py
# DESC: use Selenium + Python to automate MyData Delete flow with No Product in PROD
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException, NoSuchElementException

# ---------- ---------- ---------- ---------- ---------- 
# CONSTANTS
# ---------- ---------- ---------- ---------- ----------
WAIT_TIMEOUT = 30 
IAM_AUTH_URL_PROD = 'https://accounts.intuit.com/'
TEST_USERNAME = 'iamtestpass_1583773001901' # (new user 3/9) products: []
TEST_USERPASS = 'Intuit01-'

# ---------- ---------- ---------- ---------- ---------- 
# BROWSER-SPECIFIC WEB DRIVERS
# ---------- ---------- ---------- ---------- ---------- 

# FIREFOX - geckodriver
# browser = webdriver.Firefox()

# CHROME chromedriver (80)
options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" 
chrome_driver_binary = "/usr/local/bin/chromedriver"
browser = webdriver.Chrome(chrome_driver_binary, chrome_options=options)

# ---------- ---------- ---------- ---------- ----------  
# UTILITY METHODS
# ---------- ---------- ---------- ---------- ----------

def wait_for_elem_select(selector):
    return WebDriverWait(browser, WAIT_TIMEOUT).until(lambda browser: browser.find_element_by_css_selector(selector))

# ---------- ---------- ---------- ---------- ---------- 
# SCRIPT LOGIC 
# ---------- ---------- ---------- ---------- ----------

# Tests Auth Delete Flow (No Products) in PROD
while True:
    try:
        browser.get(IAM_AUTH_URL_PROD)
        browser.maximize_window()

        # 1: Login to Auth
        wait_for_elem_select('#ius-userid').send_keys(TEST_USERNAME)
        wait_for_elem_select('#ius-password').send_keys(TEST_USERPASS)
        sleep(3)
        wait_for_elem_select('button[name="SignIn"]').click()

        # 2: Click Data & Privacy, Delete
        sleep(8)
        WebDriverWait(browser, WAIT_TIMEOUT).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-automation="deleteManager-Continue-button"]'))).click()

        # 3: Move thru the Delete Flow Pages (No Products)
        # 3.1: Primer Page
        sleep(3)
        wait_for_elem_select('button[data-automation="continue-button"]').click()

        # 3.2: Start Page 
        sleep(3)
        wait_for_elem_select('button[class*="idsButton--primary"]').click()

        # 3.3: Delete Acknowledgement Page
        sleep(3)
        wait_for_elem_select('input[class="idsCheckbox__input"]').click()
        wait_for_elem_select('button[data-automation="continue-button"]').click()

        # 3.4: Delete Confirm Page (No Products)
        sleep(3)
        wait_for_elem_select('input[data-automation="password-field"]').send_keys(TEST_USERPASS)
        wait_for_elem_select('button[data-automation="delete-button"]').click()

        # 3.5: Success Page
        sleep(3)
        wait_for_elem_select('button[data-automation="done-button"]').click()

        # 3.6: Back on Cards Page, Click Data & Privacy, Delete Continue, then Cancel Request
        sleep(8)
        WebDriverWait(browser, WAIT_TIMEOUT).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-automation="deleteManager-Continue-button"]'))).click()
        wait_for_elem_select('button[data-automation="cancel-request-button"]').click()

        # 3.7: Cancel Request Page
        sleep(3)
        wait_for_elem_select('button[data-automation="cancel-request-button"]').click()

        # 3.8: Cancel Request Confirm Page
        sleep(3)
        wait_for_elem_select('button[data-automation="close-button"]').click()

    except TimeoutException:
        print("Oops - got a TimeoutException...let's try again")
        continue 
    except NoSuchElementException:
        print("Drat - DOM Element Not Found -- Time to Die!")
        break
    else:
        print("Script ran with No Exceptions")
    finally:
        # Cleanup 
        print("About to close the browser")
        sleep(3)
        browser.close()
        break