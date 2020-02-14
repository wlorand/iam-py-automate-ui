# FILE: iam_findmydata_fillout.py
# DESC: use Selenium with Python to automate filling out FindMyData form
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

# ------------------------------------------------------------------------------
#                                  CONSTANTS
# ------------------------------------------------------------------------------
IAM_FINDMYDATA_URL_E2E = 'https://accounts-e2e.intuit.com/app/findmydata'
NONAUTH_TEST_PERSON = {
    'email':'ashley@rush.com',
    'dob':'03191968',
    'phone':'4155179236',
    'fname':'Ashley',
	'lname':'Zzelkova',
	'address':'270 Rue Olier',
	'apt':'JJ',
	'city':'Truckee',
    'zip':'44669',
}

# ------------------------------------------------------------------------------
#                            BROWSER-SPECIFIC WEB DRIVERS
# ------------------------------------------------------------------------------

# FIREFOX - geckodriver
# browser = webdriver.Firefox()
# browser_name = 'firefox'

# CHROME chromedriver (80)
options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" 
chrome_driver_binary = "/usr/local/bin/chromedriver"
browser = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
browser_name = 'chrome'

# ------------------------------------------------------------------------------
#                                SCRIPT LOGIC
# ------------------------------------------------------------------------------

# Tests Auth Login on E2E
#
# 1. Start Flow with a GET for the URL
# 2. Fill Out All Form Fields
# 3. Click "Continue"
browser.get(IAM_FINDMYDATA_URL_E2E)
browser.maximize_window()


# Wait 10 Seconds for the Page to Load and DOM to be ready
# TODO: Replace this with WebDriver Wait utility method - try final field - DOM ready
sleep(10)

# Find Input Elements and Enter Text, Make Selection
email_field = browser.find_element_by_css_selector('[data-automation="email-address-text-field"]')
email_field.send_keys(NONAUTH_TEST_PERSON['email'])

dob_field = browser.find_element_by_css_selector('[data-automation="birthDate-text-field"]')
dob_field.send_keys(NONAUTH_TEST_PERSON['dob'])

phone_field = browser.find_element_by_css_selector('[data-automation="phone-number-text-field"]')
phone_field.send_keys(NONAUTH_TEST_PERSON['phone'])

fname_field = browser.find_element_by_css_selector('[data-automation="first-name-text-field"]')
fname_field.send_keys(NONAUTH_TEST_PERSON['fname'])

lname_field = browser.find_element_by_css_selector('[data-automation="last-name-text-field"]')
lname_field.send_keys(NONAUTH_TEST_PERSON['lname'])

address_field = browser.find_element_by_css_selector('[data-automation="address-text-field"]')
address_field.send_keys(NONAUTH_TEST_PERSON['address'])

apt_field = browser.find_element_by_css_selector('[data-automation="apt-number-text-field"]')
apt_field.send_keys(NONAUTH_TEST_PERSON['apt'])

city_field = browser.find_element_by_css_selector('[data-automation="city-text-field"]')
city_field.send_keys(NONAUTH_TEST_PERSON['city'])

# State has wonky IDS <Dropdown> that looks like a <select> but is not one
state_field = browser.find_element_by_css_selector('[data-automation="state-text-field"]')
state_field.click()

# Chrome needs a 2nd Click - but Firefox will close the menu with a 2nd click
if browser_name == 'chrome':
    state_field.click() 

sleep(3)
state_selection = browser.find_element_by_css_selector('[value="California"]')
state_selection.click()

zip_field = browser.find_element_by_css_selector('[data-automation="zip-code-text-field"]')
zip_field.send_keys(NONAUTH_TEST_PERSON['zip'])
# Hit Tab to enable Continue Button 
zip_field.send_keys(Keys.TAB) 

# Click Continue Btn
sleep(5) # see if continue button enabled
continue_btn = browser.find_element_by_css_selector('[data-automation="continue-button"]')
continue_btn.click()

# Cleanup and Close Browser
sleep(10)
print("All is Good, About to close the browser")
browser.close()
