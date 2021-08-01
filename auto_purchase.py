# 必要なもの
# pip install requests
# pip install selenium
# pip install beautifulsoup4
# chrome webdriver

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
import sys

driver = webdriver.Chrome()
amazon_id = "Enter the your amazon id"
amazon_ps = "Enter the your amazon pass"

# 商品URL
driver.get('https://www.amazon.co.jp/dp/B08GGGBKRQ/ref=cm_sw_r_apan_glt_i_04FZHAHDZPVFPYM0K9HF')

page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

if soup.find(id="shipsFromSoldBy_feature_div").find("a"):
    id_merchant_info = soup.find(id="shipsFromSoldBy_feature_div").find("a").string
    print(id_merchant_info)
else :
    driver.quit()
    sys.exit()


# 発送元がAmazon.co.jpなら購入 それ以外なら購入しない
if id_merchant_info == ("Amazon.co.jp"):
    print("買う")
else :
    print("買わない")
    driver.quit()
    sys.exit()

elem_login_btn = driver.find_element_by_xpath('//*[@id="buy-now-button"]')
elem_login_btn.click()

elem_mail = driver.find_element_by_xpath('//*[@id="ap_email"]')
elem_mail.send_keys(amazon_id)
continue_btn = driver.find_element_by_xpath('//*[@id="continue"]')
continue_btn.click()

elem_password = driver.find_element_by_xpath('//*[@id="ap_password"]')
elem_password.send_keys(amazon_ps)
submit_btn = driver.find_element_by_xpath('//*[@id="signInSubmit"]')
submit_btn.click()

# # 支払い方法（ギフト券の方はここでギフト券に切り替えて下さい）
# submit_btn2 = driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[3]/div/div[2]/div[1]/form/div[2]/div/div/div/span/span/input')
# submit_btn2.click()

# # お急ぎ便があるケース
# submit_btn3 = driver.find_element_by_xpath('//*[@id="shippingOptionFormId"]/div[1]/div[2]/div/span[1]/span/input')
# submit_btn3.click()

order_btn = driver.find_element_by_xpath('//*[@id="placeYourOrder"]/span/input')

# 購入確定ボタン
order_btn.click()

driver.quit()
sys.exit()
