#!/usr/bin/env python

import os
import dotenv
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--test-type')
options.add_argument("--disable-notifications")
options.binary_location = '/usr/bin/chromium'
driver = webdriver.Chrome(options=options)


def login(url='https://www.facebook.com'):
    dotenv.load_dotenv()
    
    driver.get(url)

    email_field = driver.find_element_by_id('email')
    email_field.send_keys(os.getenv('FB_EMAIL'))

    pass_field = driver.find_element_by_id('pass')
    pass_field.send_keys(os.getenv('FB_PASS'))
    
    login_button = driver.find_element_by_id('u_0_b')
    login_button.click()
    
    sleep(1)


def manage_posts_page(url="https://wwww.facebook.com/profile"):
    driver.get(url)

    sleep(1)
    manage_posts_xpath = '/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]' \
                         '/div[1]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div/a'
    manage_posts_btn = driver.find_element_by_xpath(manage_posts_xpath)
    driver.execute_script("arguments[0].click();", manage_posts_btn)


def profile_pics_page(url="https://wwww.facebook.com/photos"):
    driver.get(url)

    sleep(2)

    albums_tab_link = driver.find_element_by_id('u_0_1y')
    albums_tab_link.click()

    sleep(1)

    # Click into Profile Pictures Page
    spans = driver.find_elements_by_tag_name('span')
    for span in spans:
        if span.get_attribute("innerHTML") == 'Profile Pictures':
            break
    driver.execute_script("arguments[0].click();", span)

    sleep(1)


def delete_profile_pics():
    while True:
        try:
            toggle_menu = driver.find_elements_by_class_name('fbTimelineSelectorButton')[1]
        except NoSuchElementException:
            print("Can't Find PFP Element")
            break

        driver.execute_script("arguments[0].click();", toggle_menu)

        sleep(2)

        delete_option = driver.find_element_by_xpath('//a[@data-action-type="delete_photo"]')
        delete_option.click()

        sleep(1)

        buttons = driver.find_elements_by_xpath('//button[@type="submit"]')
        for btn in buttons:
            if 'layerConfirm uiOverlayButton' in btn.get_attribute('class'):
                break
        btn.click()

        sleep(3)


def delete_posts_loop():
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

        sleep(1)

        delete_all_radio_css_sel = 'body > div._10._d2i.uiLayer._4-hy._3qw > div._59s7 > div > div > div > div > div ' \
                                   '> div > div._jmh > div > ul > div:nth-child(3) > div '
        delete_all_radio_btn = driver.find_element_by_css_selector(delete_all_radio_css_sel)
        # driver.execute_script("arguments[0].click();", delete_all_radio_btn)
        delete_all_radio_btn.click()

        sleep(1)

        manage_posts_next_done_css_sel = 'body > div._10._d2i.uiLayer._4-hy._3qw > div._59s7 > div > div > div > div ' \
                                         '> div > div > div._4iyh._2pia._2pi4 > span._4iyi > div > div:nth-child(2) >' \
                                         ' button '
        manage_posts_next_done_btn = driver.find_element_by_css_selector(manage_posts_next_done_css_sel)
        manage_posts_next_done_btn.click()
        sleep(2)
        manage_posts_next_done_btn.click()

        sleep(10)


login()

# TODO Delete Profile Pics
profile_pics_page()
test = delete_profile_pics()


# manage_posts_page()
# delete_posts_loop()

