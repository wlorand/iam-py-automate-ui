# FILE: iam_security_card_add_info_auto_e2e.py
# DESC: use Selenium + Python to automate IAM Security Card Add Info in E2E
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
IAM_AUTH_URL_E2E = 'https://accounts-e2e.intuit.com/index.html?iux_v3=true'
# NOTE: New User must be created (test-easy) and pasted here for repeatability
TEST_USERNAME = 'iamtestpass_1585850964306' 
TEST_USERPASS = 'Intuit01-'
TEST_SECURITY_ADD_INFO = {
    'phone': '8183336099'
}

# ---------- ---------- ---------- ---------- ---------- 
# BROWSER-SPECIFIC WEB DRIVERS
# ---------- ---------- ---------- ---------- ---------- 

# FIREFOX - geckodriver
# browser = webdriver.Firefox()
# browser_name = 'firefox'

# CHROME chromedriver (v80)
options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" 
chrome_driver_binary = "/usr/local/bin/chromedriver"
browser = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
browser_name = 'chrome'

# ---------- ---------- ---------- ---------- ----------  
# UTILITY METHODS
# ---------- ---------- ---------- ---------- ----------

def wait_for_elem_select(selector):
    return WebDriverWait(browser, WAIT_TIMEOUT).until(lambda browser: browser.find_element_by_css_selector(selector))

# ---------- ---------- ---------- ---------- ---------- 
# SCRIPT LOGIC 
# ---------- ---------- ---------- ---------- ----------

# Tests IAM Security Card User Interactions
while True:
    try:
        browser.get(IAM_AUTH_URL_E2E)
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
    
        # 2: Security Card > Add Phone Interaction 
        # 2.0: Scroll Down to Security Card
        browser.execute_script("window.scrollTo(0, 275);")
        sleep(3)

        if browser_name == 'firefox':
            # 2.1: Add Flow: Click 'Add Phone'
            # option 1: use link_text - poc (only possible as dom element is <a> tag)
            # browser.find_element_by_link_text('Add Phone').click()
            # WebDriverWait(browser, WAIT_TIMEOUT).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Add Phone'))).click()
            # option 2: use id selector
            wait_for_elem_select('a[id="ius-phone-manager-view-mode-add-phone"]').click()

            # 2.2: Add Flow: Enter Phone and Password
            wait_for_elem_select('input[id="ius-phone-manager-new-phone"]').send_keys(TEST_SECURITY_ADD_INFO['phone'])
            wait_for_elem_select('input[id="ius-phone-current-password"]').send_keys(TEST_USERPASS)

            # 2.3: Add Flow: Click Save
            sleep(3)
            wait_for_elem_select('input[id="ius-phone-manager-btn-submit"]').click()

            # 2.4: Add Flow: Skip Verification and Click Close x 2 (will save new phone and close phone widget)
            wait_for_elem_select('button[id="ius-phone-manager-btn-cancel"]').click()
            sleep(5)
            wait_for_elem_select('button[id="ius-phone-manager-btn-cancel"]').click()
        
        # 3: Add Flow: save screenshot (png)
        sleep(5)
        if browser_name == 'firefox':
            browser.save_screenshot('screenshots/security-card-add-auto-firefox-e2e.png')
        elif browser_name == 'chrome':
            browser.save_screenshot('screenshots/security-card-add-auto-chrome-e2e.png')

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
