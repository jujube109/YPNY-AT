from page.login_page import Login_Page
from selenium import webdriver
import unittest
from lib.Parametric import Get_Parametric
import time
from page.data_sim import SimAddPage
import random
from lib.phonenumber import PhoneNum


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.pa = Get_Parametric()
        self.url = self.pa.get_url_value("back_login_url")
        self.user_account = self.pa.get_user_account()
        self.username_path = self.pa.get_emelent_path("back_username")
        self.password_path = self.pa.get_emelent_path("back_password")
        self.verify_path = self.pa.get_emelent_path("verify_code")
        self.button_path = self.pa.get_emelent_path("confirm_button")
        self.topic_path = self.pa.get_emelent_path("topica_path")
        self.sim_button = self.pa.get_emelent_path("SIM_button")
        self.sim_addbutton = self.pa.get_emelent_path("sim_add_button")
        self.isplist_button = self.pa.get_emelent_path("isplist_buttonpath")
        self.isps_text = self.pa.get_emelent_path("isps_text")
        self.sim_ownerpath = self.pa.get_emelent_path("sim_ownerpath")
        self.phone_path = self.pa.get_emelent_path("phone_path")
        self.confirm = self.pa.get_emelent_path("confirm")

    def test01_addSim(self):
        driver = self.driver
        lo = Login_Page(driver)
        sm = SimAddPage(driver)
        lo.login_url(self.url)
        lo.login_input(self.username_path, self.user_account[0],
                       self.password_path, self.user_account[1],
                       self.verify_path, "6666",
                       self.button_path)

        # driver.maximize_window()
        time.sleep(1)
        sm.clicktopica(self.topic_path)
        time.sleep(1)
        sm.click_sim(self.sim_button)
        time.sleep(1)
        sm.simAddButton(self.sim_addbutton)
        time.sleep(1)
        isptext = sm.ispChoice(self.isplist_button, self.isps_text)
        owner_value = ''.join(random.sample([chr(i) for i in range(97, 123)], 5))
        print(owner_value)
        sm.simOwner(self.sim_ownerpath, owner_value)
        pm = PhoneNum()
        if isptext == "中国移动":
            phone = pm.yiDong()
            sm.phoneNum(self.phone_path, phone)
        elif isptext == "中国联通":
            phone = pm.lianTong()
            sm.phoneNum(self.phone_path, phone)
        elif isptext == "中国电信":
            phone = pm.dianXin()
            sm.phoneNum(self.phone_path, phone)
        else:
            print("未获取到运营商文本")
        sm.confirm(self.confirm)
        time.sleep(1)
        check_ism = sm.checkIsm(self.pa.get_emelent_path("check_Ism"))
        check_owner = sm.checkOwner(self.pa.get_emelent_path("check_ownerpath"))
        print(check_ism, check_owner)
        flag = False
        if check_owner == owner_value and check_ism == isptext:
            flag = True
        self.assertTrue(flag)