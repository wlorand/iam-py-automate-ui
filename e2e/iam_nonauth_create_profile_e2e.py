# FILE: iam_nonauth_create_profile_e2e.py
# DESC: use Selenium + Python to automate  NonAuth Create Profile (Find My Data) in E2E
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait # for refactor
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import TimeoutException, NoSuchElementException

# ---------- ---------- ---------- ---------- ---------- 
# CONSTANTS
# ---------- ---------- ---------- ---------- ----------

WAIT_TIMEOUT = 30 
IAM_FINDMYDATA_URL_E2E = 'https://accounts-e2e.intuit.com/app/findmydata'
NONAUTH_TEST_PERSON = {
    'email' : 'ashley@rush.com',
    'dob' : '03191968',
    'phone' : '4155179236',
    'fname' : 'Ashley',
	'lname' : 'Zzelkova',
	'address' : '270 Rue Olier',
	'apt' : 'JJ',
	'city' : 'Truckee',
    'zip' : '44669',
}

# ---------- ---------- ---------- ---------- ---------- 
# BROWSER-SPECIFIC WEB DRIVERS
# ---------- ---------- ---------- ---------- ---------- 

# FIREFOX - geckodriver
browser = webdriver.Firefox()
browser_name = 'firefox'

# CHROME chromedriver (80)
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

# ---------- ---------- ---------- ---------- ---------- 
# SCRIPT LOGIC 
# ---------- ---------- ---------- ---------- ----------

# Tests NonAuth Create Profile (Find My Data Form Submission)
while True:
    try:
        browser.get(IAM_FINDMYDATA_URL_E2E)
        browser.maximize_window()

        # Fill out all form fields with NONAUTH_TEST_PERSON data
        wait_for_elem_select('input[data-automation="email-address-text-field"]').send_keys(NONAUTH_TEST_PERSON['email'])
        wait_for_elem_select('input[data-automation="birthDate-text-field"]').send_keys(NONAUTH_TEST_PERSON['dob'])
        wait_for_elem_select('input[data-automation="phone-number-text-field"]').send_keys(NONAUTH_TEST_PERSON['phone'])
        wait_for_elem_select('input[data-automation="first-name-text-field"]').send_keys(NONAUTH_TEST_PERSON['fname'])
        wait_for_elem_select('input[data-automation="last-name-text-field"]').send_keys(NONAUTH_TEST_PERSON['lname'])
        wait_for_elem_select('input[data-automation="address-text-field"]').send_keys(NONAUTH_TEST_PERSON['address'])
        wait_for_elem_select('input[data-automation="apt-number-text-field"]').send_keys(NONAUTH_TEST_PERSON['apt'])
        wait_for_elem_select('input[data-automation="city-text-field"]').send_keys(NONAUTH_TEST_PERSON['city'])

        # State Field has wonky IDS <Dropdown> that looks like a <select> but is not one
        state_field = browser.find_element_by_css_selector('input[data-automation="state-text-field"]')
        state_field.click()
        # Conditional 2nd Click: Chrome needs a 2nd Click - but Firefox will close the menu with a 2nd click
        if browser_name == 'chrome':
            state_field.click() 
        wait_for_elem_select('div[value="California"]').click()

        # After zip field text entry, Hit Tab to enable Continue Button and Submit Form
        wait_for_elem_select('input[data-automation="zip-code-text-field"]').send_keys(NONAUTH_TEST_PERSON['zip'])
        wait_for_elem_select('input[data-automation="zip-code-text-field"]').send_keys(Keys.TAB) 
        sleep(3) # see continue button enabled
        wait_for_elem_select('button[data-automation="continue-button"]').click()

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
