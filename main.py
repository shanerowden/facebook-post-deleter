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

# scroll_to_bottom_js = '''interval = setInterval(function() {
#                             window.scrollTo(0, document.body.scrollHeight);
#                         }, 1000);'''
# driver.execute_script(scroll_to_bottom_js)


while True:
    posts_by_you_xpath = '//*[@id="timeline_overview"]/div[2]/div[1]/div/div/div/a[2]'
    posts_by_you_toggle = driver.find_element_by_xpath(posts_by_you_xpath)
    driver.execute_script("arguments[0].click();", posts_by_you_toggle)

    sleep(1)

    all_in_month_xpath = '//*[@id="timeline_overview"]/div[2]/div[2]/div[1]/div/div[1]/div/div/label/button'
    all_in_month_checkbox = driver.find_element_by_xpath(all_in_month_xpath)
    driver.execute_script("arguments[0].click();", all_in_month_checkbox)

    sleep(1)

    manage_posts_next_xpath = '//*[@id="timeline_overview"]/div[2]/div[2]/div[2]/div[2]/div/button/div/div'
    manage_posts_next_btn = driver.find_element_by_xpath(manage_posts_next_xpath)
    driver.execute_script("arguments[0].click();", manage_posts_next_btn)

    sleep(3)

    delete_all_radio_css_sel = 'body > div._10._d2i.uiLayer._4-hy._3qw > div._59s7 > div > div > div > div > div > div > div._jmh > div > ul > div:nth-child(3) > div'
    delete_all_radio_btn = driver.find_element_by_css_selector(delete_all_radio_css_sel)
    # driver.execute_script("arguments[0].click();", delete_all_radio_btn)
    delete_all_radio_btn.click()

    sleep(1)

    manage_posts_next_done_css_sel = 'body > div._10._d2i.uiLayer._4-hy._3qw > div._59s7 > div > div > div > div > div > div > div._4iyh._2pia._2pi4 > span._4iyi > div > div:nth-child(2) > button'
    manage_posts_next_done_btn = driver.find_element_by_css_selector(manage_posts_next_done_css_sel)
    manage_posts_next_done_btn.click()
    sleep(2)
    manage_posts_next_done_btn.click()

    sleep(10)

# TODO Select and Toggle Every Post
# TODO Select Delete Button and Click

