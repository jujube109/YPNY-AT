from selenium import  webdriver

from PIL import ImageGrab
import pyzbar.pyzbar as pybar
import time

driver = webdriver.Chrome()
driver.get("http://192.168.0.110:8960/#/login")

driver.find_element_by_id("tab-code").click()
time.sleep(1)
token = ''
im = ImageGrab.grab()
print(im)
txt_list = pybar.decode(im)
print(txt_list)
for txt in txt_list:
    token = txt.data.decode()
    print(token)




