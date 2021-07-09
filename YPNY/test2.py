from selenium import  webdriver

from page.devices_parameter import BuiltParameter
from lib.Parametric import Get_Parametric
from page.login_page import Login_Page
import time
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
lb=Get_Parametric()
username_path = lb.get_emelent_path("back_username")
password_path =lb.get_emelent_path("back_password")
verify_path = lb.get_emelent_path("verify_code")
button_path = lb.get_emelent_path("confirm_button")
user_account=lb.get_user_account()
factory_path = lb.get_emelent_path("factory_path")
BP_button=lb.get_emelent_path("BP_button")
BP_addbuttion=lb.get_emelent_path("BP_addButton")
url = lb.get_url_value("back_login_url")
BP_inputname=lb.get_emelent_path("BP_NameInput")
BP_inputtype=lb.get_emelent_path("BP_TypeInput")
BP_lipath=lb.get_emelent_path("BP_lipath")
print(BP_lipath)
login=Login_Page(driver)
BP=BuiltParameter(driver)
login.login_url(url)
login.login_input(username_path,user_account[0],
                       password_path,user_account[1],
                       verify_path, "6666",
                       button_path)
time.sleep(1)

BP.wait((By.XPATH,factory_path))
BP.click_factory(factory_path)
BP.wait((By.XPATH,BP_button))
BP.click_BuiltParameter(BP_button)
BP.wait((By.CSS_SELECTOR,BP_addbuttion))
BP.add_button(BP_addbuttion)
BP.input_ParameterName(BP_inputname,"测试参数1")
BP.choice_ParameterType(BP_inputtype,BP_lipath)


driver.close()


