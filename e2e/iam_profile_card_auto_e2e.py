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
# IAM_AUTH_URL_LOCAL = 'https://accounts-e2e.intuit.com/index.html?iam-account-manager-ui.local=true'
TEST_USERNAME = 'iamtestpass_1585086735359'  # Add Flow test user 
TEST_USERPASS = 'Intuit01-'

# ---------- ---------- ---------- ---------- ---------- 
# BROWSER-SPECIFIC WEB DRIVERS
# ---------- ---------- ---------- ---------- ---------- 

# FIREFOX - geckodriver
browser = webdriver.Firefox()
browser_name = 'firefox'

# CHROME chromedriver (v80)
# options = webdriver.ChromeOptions()
# options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" 
# chrome_driver_binary = "/usr/local/bin/chromedriver"
# browser = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
# browser_name = 'chrome'

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

# Tests IAM Profile Card User Interactions
while True:
    try:
        browser.get(IAM_AUTH_URL_E2E)
        # browser.get(IAM_AUTH_URL_LOCAL)
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
        if browser_name == 'firefox':
            browser.execute_script("window.scrollTo(0, 850);") 
        elif browser_name == 'chrome':
            browser.execute_script("window.scrollTo(0, 900);") # account for chrome automated software ribbon
        else:
            browser.execute_script("window.scrollTo(0, 850);")
        sleep(3)

        # 2.1: Add Flow: Click 'Add Your Name'
        sleep(3)
        WebDriverWait(browser, WAIT_TIMEOUT).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-automation="iam-add-name-link-btn"]'))).click()

        # 2.2: Add Flow: Enter Name 
        wait_for_elem_select('input[id="ius-first-name"]').send_keys('Vincent')
        wait_for_elem_select('input[id="ius-last-name"]').send_keys('Vega')
        
        # 2.3 Add Flow: Name: Click Save (will collapse name widget)
        sleep(3)
        wait_for_elem_select('button[id="ius-fullname-manager-btn-save"]').click()
        
        # 3.0: Locate DOM Elements, save as PY List (no unique DOM handle exists to locate required element)
        add_link_buttons = wait_for_elements_select('button[data-automation="iam-collapsible-product-link-btn"]')
        print(len(add_link_buttons)) # 2 (1- Add your DOB; 2- Add Your occupation)
        
        # 3.1: Add Flow: Click 'Add Your Date of Birth'
        sleep(3)
        add_link_buttons[0].click() # should open the DOB widget

        # 3.2: Add Flow: Enter DOB 
        wait_for_elem_select('input[id="dob-input-form-field"]').send_keys('05/05/1975')

        # 3.3: Add Flow: DOB:  Click Save (will collapse DOB widget)
        sleep(3)
        wait_for_elem_select('button[id="dob-save-btn"]').click()

        # 4.1: Add Flow: Click 'Add Your Occupation'
        sleep(3)
        add_link_buttons[1].click()

        # 4.2: Add Flow: Enter Occupation
        wait_for_elem_select('input[id="occupation-input-form-field"]').send_keys('Fictional Hitman')

        # 4.3: Add Flow: Occupation: Click Save (will collapse Occupation widget)
        sleep(3)
        wait_for_elem_select('button[id="occupation-save-btn"]').click()
        
        # 5.1: Add Flow: Click 'Add Your Address'
        sleep(3)
        wait_for_elem_select('button[data-automation="iam-add-address-link-btn"]').click()
        # Scroll Down 300 pixels
        browser.execute_script("window.scrollBy(0, 300);")
        
        # 5.2: Add Flow: Fill in Address Fields
        # 5.2.1: Country (+ TAB)
        sleep(3)
        wait_for_elem_select('input[data-automation="ius-country"]').send_keys('United States')
        wait_for_elem_select('input[data-automation="ius-country"]').send_keys(Keys.TAB)
        # 5.2.2: Street Address
        wait_for_elem_select('input[id="ius-street"]').send_keys('33 Emerald Street')
        # 5.2.3: Address Line 2
        wait_for_elem_select('input[id="ius-street-2"]').send_keys('Suite 666')
        # 5.2.4: City
        wait_for_elem_select('input[id="ius-city"]').send_keys('Redondo Beach')
        # 5.2.5: State (+ TAB)
        wait_for_elem_select('input[id="idsDropdownTypeaheadTextField4"]').send_keys('California')
        wait_for_elem_select('input[id="idsDropdownTypeaheadTextField4"]').send_keys(Keys.TAB)
        # 5.2.6: Zip
        wait_for_elem_select('input[id="ius-zip-code"]').send_keys('90277')
        # 5.3: Add Flow: Address: Click Save (will collapse Address widget)
        sleep(3)
        wait_for_elem_select('button[id="ius-address-manager-btn-save"]').click()

        # 9: Add Flow: save screenshot (png)
        sleep(5)
        if browser_name == 'firefox':
            browser.save_screenshot('screenshots/iam-profile-card-auto-firefox-e2e.png')
        elif browser_name == 'chrome':
            browser.save_screenshot('screenshots/iam-profile-card-auto-chrome-e2e.png')

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