# FILE: iam_security_card_edit_info_auto_e2e.py
# DESC: use Selenium + Python to automate IAM Security Card Edit Info in E2E
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
# TODO: Create original_security_settings {} and changed_security_settings {} for toggle betw credentials - makes script truly repeatable
TEST_USERNAME = 'iamtestpass_1585850964308' #  8
TEST_USERPASS = 'Intuit03-' # 3
TEST_SECURITY_NEW_INFO = {
    'new_username': 'iamtestpass_1585850964309', # next: 9
    'new_password': 'Intuit03-', # 4 - go up down the line for now 
    'new_email': 'testeasy1585850964301@blackhole.intuit.com', # 1
    'new_phone': '8183336096' # 6 - next, go backwards down the number line
}

TEST_SECURITY_ORIGINAL_INFO = {
    'orig_username': TEST_USERNAME,
    'orig_password': TEST_USERPASS,
    'orig_email': 'testeasy1585850964306@blackhole.intuit.com',
    'orig_phone': '8183336097' # now 7 - new original #  
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

# Tests IAM Security Card User Interactions: Edie Flow
# NOTE: Script needs an account with Phone Added (either manually or by running the add_info py script)
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
        sleep(10)
        assert 'Intuit Accounts - Account Manager' in browser.title 
    
        # 2: Security Card > Edit Flow
        # 2.0: Scroll Down to Security Card
        browser.execute_script("window.scrollTo(0, 275);")
        sleep(3)
        
        # EDIT USER ID
        # # 2.1: Edit Flow > User ID: Click 'Edit'
        # wait_for_elem_select('button[id="ius-user-id-manager-btn-update"]').click()
        # # 2.2: Edit User ID: Clear field and Enter New User ID
        # sleep(3)
        # WebDriverWait(browser, WAIT_TIMEOUT).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="ius-user-id-manager-new-user-id"]'))).clear()
        # wait_for_elem_select('input[id="ius-user-id-manager-new-user-id"]').send_keys(TEST_SECURITY_NEW_INFO['new_username'])
        # # 2.3: Edit User ID: Enter Password
        # wait_for_elem_select('input[id="ius-user-id-current-password"]').send_keys(TEST_USERPASS)
        # # 2.4: Edit User ID: Click Save Btn (collapses mini-widget)
        # sleep(3)
        # wait_for_elem_select('input[id="ius-user-id-manager-btn-submit"]').click()

        # EDIT EMAIL
        # # 3.1: Edit Flow > Email Address: Click 'Edit'
        # wait_for_elem_select('button[id="ius-email-manager-btn-update"]').click()
        # # 3.2: Edit Email: Clear field and Enter New Email
        # sleep(3)
        # WebDriverWait(browser, WAIT_TIMEOUT).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="ius-email-manager-new-email"]'))).clear()
        # wait_for_elem_select('input[id="ius-email-manager-new-email"]').send_keys(TEST_SECURITY_NEW_INFO['new_email'])
        # # 3.3: Edit Email: Confirm New Email
        # wait_for_elem_select('input[id="ius-email-manager-new-email-confirm"]').send_keys(TEST_SECURITY_NEW_INFO['new_email'])
        # # 3.4: Edit Email: Enter Password
        # wait_for_elem_select('input[id="ius-email-current-password"]').send_keys(TEST_USERPASS)
        # # 3.5: Edit Email: Click Save Btn 
        # sleep(3)
        # wait_for_elem_select('input[id="ius-email-manager-btn-submit"]').click()
        # # 3.6: Edit Email: Blow off Email Verify, Click Close (collapses mini-widget)
        # sleep(5)
        # wait_for_elem_select('a[id="ius-email-manager-edit-view-verify-email-sent-btn-cancel"]').click()

        # EDIT PASSWORD
        # 4.1: Edit Flow > Password: Click 'Edit'
        wait_for_elem_select('button[data-automation="iam-edit-password-link-btn"]').click()
        # 4.2: Edit Password: Enter New Password
        sleep(3)
        WebDriverWait(browser, WAIT_TIMEOUT).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="idsTxtField3"]'))).send_keys(TEST_SECURITY_NEW_INFO['new_password'])
        # # 4.3: Edit Password: Confirm New Password
        wait_for_elem_select('input[id="idsTxtField6"]').send_keys(TEST_SECURITY_NEW_INFO['new_password'])
        # # 4.4: Edit Password: Enter Current Password
        wait_for_elem_select('input[id="idsTxtField9"]').send_keys(TEST_USERPASS)
        # # 4.5: Edit Password: Click Save Btn (collapses mini-widget)
        sleep(3)
        wait_for_elem_select('button[class*="idsButton--primary"]').click()
        
        # # EDIT PHONE
        # # 5.1: Edit Flow > Phone: Click 'Edit'
        # wait_for_elem_select('button[id="ius-phone-manager-btn-update"]').click()
        # # 5.2: Edit Phone: Blow Off Verify & Click small Change Link
        # sleep(3)
        # browser.find_element_by_link_text('Change').click()
        # # 5.3: Edit Phone: Clear field and Enter New Phone
        # sleep(3)
        # WebDriverWait(browser, WAIT_TIMEOUT).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="ius-phone-manager-new-phone"]'))).clear()
        # wait_for_elem_select('input[id="ius-phone-manager-new-phone"]').send_keys(TEST_SECURITY_NEW_INFO['new_phone'])
        # # 5.4: Edit Phone: Enter Password (likely new password - good sanity test for entering changed password)
        # wait_for_elem_select('input[id="ius-phone-current-password"]').send_keys(TEST_USERPASS)
        # # 5.5: Edit Phone: Click Save Btn  
        # sleep(3)
        # wait_for_elem_select('input[id="ius-phone-manager-btn-submit"]').click()
        # # 5.6: Edit Phone: Blow off Verify and Click Close (should save phone and close mini-widget)
        # sleep(5)
        # wait_for_elem_select('button[id="ius-phone-manager-btn-cancel"]').click()

        # 6: Edit Flow: save screenshot (png)
        sleep(5)
        if browser_name == 'firefox':
            browser.save_screenshot('screenshots/security-card-edit-auto-firefox-e2e.png')
        elif browser_name == 'chrome':
            browser.save_screenshot('screenshots/security-card-edit-auto-chrome-e2e.png')

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
