#!/usr/bin/env python

import os
import dotenv
from time import sleep

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--test-type')
options.binary_location = '/usr/bin/chromium'
driver = webdriver.Chrome(
    chrome_options=options
)

login_url = "https://wwww.facebook.com"
driver.get(login_url)

dotenv.load_dotenv()
email_field = driver.find_element_by_id('email')
email_field.send_keys(os.getenv('FB_EMAIL'))

pass_field = driver.find_element_by_id('pass')
pass_field.send_keys(os.getenv('FB_PASS'))

login_button = driver.find_element_by_id('u_0_b')
login_button.click()

sleep(1)
profile_url = "https://wwww.facebook.com/profile"
driver.get(profile_url)

sleep(1)
manage_posts_xpath = '/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]' \
                     '/div[1]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div/a'
manage_posts_btn = driver.find_element_by_xpath(manage_posts_xpath)
driver.execute_script("arguments[0].click();", manage_posts_btn)

scroll_to_bottom_js = '''interval = setInterval(function() {
                            window.scrollTo(0, document.body.scrollHeight);
                        }, 1000);'''
driver.execute_script(scroll_to_bottom_js)

# TODO Select and Toggle Every Post
# TODO Select Delete Button and Click
