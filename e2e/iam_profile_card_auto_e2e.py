# FILE: iam_profile_card_auto_e2e.py
# DESC: use Selenium + Python to automate IAM Profile Card User Interactions in E2E
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException, NoSuchElementException

# ---------- ---------- ---------- ---------- ---------- 
# CONSTANTS
# ---------- ---------- ---------- ---------- ----------
WAIT_TIMEOUT = 30 
IAM_AUTH_URL_E2E = 'https://accounts-e2e.intuit.com/'
IAM_AUTH_URL_LOCAL = 'https://accounts-e2e.intuit.com/index.html?iam-account-manager-ui.local=true'
TEST_USERNAME = 'iamtestpass_1584639773308' 
TEST_USERPASS = 'Intuit01-'

# ---------- ---------- ---------- ---------- ---------- 
# BROWSER-SPECIFIC WEB DRIVERS
# ---------- ---------- ---------- ---------- ---------- 

# FIREFOX - geckodriver
browser = webdriver.Firefox()

# CHROME chromedriver (80)
# options = webdriver.ChromeOptions()
# options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" 
# chrome_driver_binary = "/usr/local/bin/chromedriver"
# browser = webdriver.Chrome(chrome_driver_binary, chrome_options=options)

# ---------- ---------- ---------- ---------- ----------  
# UTILITY METHODS
# ---------- ---------- ---------- ---------- ----------

def wait_for_elem_select(selector):
    return WebDriverWait(browser, WAIT_TIMEOUT).until(lambda browser: browser.find_element_by_css_selector(selector))

# ---------- ---------- ---------- ---------- ---------- 
# SCRIPT LOGIC 
# ---------- ---------- ---------- ---------- ----------

# Tests IAM Profile Card User Interactions
while True:
    try:
        # browser.get(IAM_AUTH_URL_E2E)
        browser.get(IAM_AUTH_URL_LOCAL)
        browser.maximize_window()

        # 1.1: Enter User/Pass
        wait_for_elem_select('#ius-userid').send_keys(TEST_USERNAME)
        wait_for_elem_select('#ius-password').send_keys(TEST_USERPASS)

        # 1.2: Click Sign-In Button
        sleep(3)
        wait_for_elem_select('button[name="SignIn"]').click()

        # 1.3: Confirm IAM Cards Overview Page Loaded
        sleep(8)
        assert 'Intuit Accounts - Account Manager' in browser.title 
        
        
        # 2: Profile Card > Name Widget Add Interaction 
        # 2.0: Scroll Down to Profile Card
        browser.execute_script("window.scrollTo(0, 900);") # Chrome needs xtra 100 pixels (automated software ribbon)
        sleep(3)

        # 2.1: Click Add Your Name
        WebDriverWait(browser, WAIT_TIMEOUT).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-automation="iam-add-name-link-btn"]'))).click()

        # 2.2: Enter Name 
        sleep(3)
        wait_for_elem_select('input[id="ius-first-name"]').send_keys('Will')
        wait_for_elem_select('input[id="ius-last-name"]').send_keys('Cody')
        
        # 2.3 Click Save (will collapse name widget)
        sleep(3)
        wait_for_elem_select('button[id="ius-fullname-manager-btn-save"]').click()

        # temp 2.4: save screenshot (png)
        sleep(5)
        browser.save_screenshot('screenshots/iam-profile-card-name-auto-e2e.png')

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
        sleep(5)
        browser.close()
        break