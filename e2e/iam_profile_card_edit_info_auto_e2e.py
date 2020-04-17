# FILE: iam_profile_card_edit_info_auto_e2e.py
# DESC: use Selenium + Python to automate IAM Profile Card Edit Info in E2E
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
IAM_AUTH_URL_E2E = 'https://accounts-e2e.intuit.com/index.html?iux_v3=true'
TEST_USERNAME = 'iamtestpass_1585761963175' # Account with Existing Full Profile Info 
TEST_USERPASS = 'Intuit01-'
TEST_PROFILE_EDIT_INFO = {
    'fname': 'Jules',
	'lname': 'Winnfield',
	'dob': '02/02/1969',
	'occupation': 'Earthwalker-Bum',
	'country': 'United States Minor Outlying Islands', 
	'street': '1106 Crenshaw Blvd',
	'street-2': 'Suite Z',
	'city': 'Torrance',
	'state': 'California',
	'zip': '90501'
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

# return a PY List of Selenium Objects
def wait_for_elements_select(selector):
    return WebDriverWait(browser, WAIT_TIMEOUT).until(lambda browser: browser.find_elements_by_css_selector(selector))

# ---------- ---------- ---------- ---------- ---------- 
# SCRIPT LOGIC 
# ---------- ---------- ---------- ---------- ----------

# Tests IAM Profile Card User Interactions - Add Flow
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
        
        # 2: Profile Card > Name Widget Add Edit Interaction 
        # 2.0: Scroll Down to Profile Card
        browser.execute_script("window.scrollTo(0, 850);")
        sleep(3)

        if browser_name == 'firefox':
            # EDIT NAME
            # 2.1: Click 'Edit'
            wait_for_elem_select('button[data-automation="iam-edit-name-link-btn"]').click()
            # 2.2: Edit Name: clear fields 
            sleep(3)
            WebDriverWait(browser, WAIT_TIMEOUT).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="ius-first-name"]'))).clear()
            WebDriverWait(browser, WAIT_TIMEOUT).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="ius-last-name"]'))).clear()
            sleep(3)
            # 2.3: Edit Name: Enter new first name
            wait_for_elem_select('input[id="ius-first-name"]').send_keys(TEST_PROFILE_EDIT_INFO['fname'])
            # 2.4: Edit Name: Enter new last name
            wait_for_elem_select('input[id="ius-last-name"]').send_keys(TEST_PROFILE_EDIT_INFO['lname'])
            # 2.4: Edit Name: Click Save Btn (collapses mini-widget)
            sleep(3)
            wait_for_elem_select('button[id="ius-fullname-manager-btn-save"]').click()

            # EDIT DOB
            # Locate DOM Elements, save as PY List (no unique DOM handle exists to locate required element)
            edit_link_buttons = wait_for_elements_select('button[data-automation="iam-collapsible-product-link-btn"]')
            print(f'there are {len(edit_link_buttons)} edit_link_buttons on the page') # 2 (1- Add your DOB; 2- Add Your occupation)
            # 3.1: Click 'Edit' DOB
            sleep(3)
            edit_link_buttons[0].click() # should open the DOB widget
            # 3.2: Edit DOB: Clear field
            wait_for_elem_select('input[id="dob-input-form-field"]').clear() 
            # 3.3: Edit DOB: Enter new DOB
            sleep(3)
            wait_for_elem_select('input[id="dob-input-form-field"]').send_keys(TEST_PROFILE_EDIT_INFO['dob'])
            # 3.4: Edit DOB: Click Save # should close the DOB mini-widget
            sleep(3)
            wait_for_elem_select('button[id="dob-save-btn"]').click()

            # EDIT OCCUPATION
            # 4.1: Click 'Edit' Occupation
            sleep(3)
            edit_link_buttons[1].click() # should open the Occupation widget
            # 4.2: Edit Occupation: Clear field
            wait_for_elem_select('input[id="occupation-input-form-field"]').clear() 
            # 4.3: Edit Occupation: Enter new Occupation
            sleep(3)
            wait_for_elem_select('input[id="occupation-input-form-field"]').send_keys(TEST_PROFILE_EDIT_INFO['occupation'])
            # 4.4: Edit Occupation: Click Save # should close the Occupation mini-widget
            wait_for_elem_select('button[id="occupation-save-btn"]').click()
            
            # EDIT ADDRESS
            # 5.1: Click 'Edit' Address
            sleep(3)
            wait_for_elem_select('button[data-automation="iam-edit-address-link-btn"]').click()
            # 5.2: Scroll Down for Expanded Address widget
            browser.execute_script("window.scrollBy(0, 350);")
            # 5.3: Edit Address: Clear and Fill in Address Fields
            # 5.3.1: Country (+ TAB)
            wait_for_elem_select('input[data-automation="ius-country"]').clear()
            wait_for_elem_select('input[data-automation="ius-country"]').send_keys(TEST_PROFILE_EDIT_INFO['country'])
            wait_for_elem_select('input[data-automation="ius-country"]').send_keys(Keys.TAB)
            # 5.3.2: Street Address
            wait_for_elem_select('input[id="ius-street"]').clear()
            wait_for_elem_select('input[id="ius-street"]').send_keys(TEST_PROFILE_EDIT_INFO['street'])
            # 5.3.3: Address Line 2
            wait_for_elem_select('input[id="ius-street-2"]').clear()
            wait_for_elem_select('input[id="ius-street-2"]').send_keys(TEST_PROFILE_EDIT_INFO['street-2'])
            # 5.3.4: City
            wait_for_elem_select('input[id="ius-city"]').clear()
            wait_for_elem_select('input[id="ius-city"]').send_keys(TEST_PROFILE_EDIT_INFO['city'])
            # 5.3.5: State (+ TAB)
            pass  # DOM here is too wonky to deal with just now - each state has diff ID field which is diff than the empty field
            # 5.3.6: Zip
            wait_for_elem_select('input[id="ius-zip-code"]').clear()
            wait_for_elem_select('input[id="ius-zip-code"]').send_keys(TEST_PROFILE_EDIT_INFO['zip'])
            # 5.4: Edit Address: Click Save (will collapse Address widget)
            sleep(6)
            wait_for_elem_select('button[id="ius-address-manager-btn-save"]').click()
            # 5.5: Scroll Back Up for collapsed Address widget
            browser.execute_script("window.scrollBy(0, -350);")

        # 6: Add Flow: save screenshot (png)
        sleep(5)
        if browser_name == 'firefox':
            browser.save_screenshot('screenshots/profile-card-edit-auto-firefox-e2e.png')
        elif browser_name == 'chrome':
            browser.save_screenshot('screenshots/profile-card-edit-auto-chrome-e2e.png')

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
