from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

user = input('請輸入github帳號：')
pwd = input('請輸入github密碼：')

web = webdriver.Chrome(r".\\data\\chromedriver.exe")
host = 'https://github.com/'
web.set_window_position(0, 0)
web.set_window_size(800, 1045)
web.get(host)


def wait(element):
    try:
        WebDriverWait(web, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, element))
        )
    except:
        print('error:' + element + 'not found')
        web.save_screenshot('.\\pic\\error.png')
    return


def click(btn):
    wait(btn)
    newbtn = web.find_element_by_css_selector(btn)
    web.execute_script("arguments[0].click();", newbtn)
    return


def login(user, pwd):
    click(
        'body > div.position-relative.js-header-wrapper > header > div > div.HeaderMenu.HeaderMenu--logged-out.position-fixed.top-0.right-0.bottom-0.height-fit.position-lg-relative.d-lg-flex.flex-justify-between.flex-items-center.flex-auto > div.d-lg-flex.flex-items-center.px-3.px-lg-0.text-center.text-lg-left > a.HeaderMenu-link.no-underline.mr-3')
    wait('#login_field')
    web.find_element_by_css_selector('#login_field').send_keys(user)
    web.find_element_by_css_selector('#password').send_keys(pwd)
    click('#login > form > div.auth-form-body.mt-3 > input.btn.btn-primary.btn-block')
    wait('body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-lg-flex > details > summary')
    return


login(user, pwd)
