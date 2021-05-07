from selenium import webdriver
import time
import unittest
from lib.Parametric import Get_Parametric
from page.login_page import Login_Page
from page.devices_components import Components
import os
import random


class ComponentsTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.pa = Get_Parametric()
        self.topic_path = self.pa.get_emelent_path("topica_path")
        self.collection_path = self.pa.get_emelent_path("collection_path")
        self.collectionAdd_path = self.pa.get_emelent_path("collection_add_button")
        self.url = self.pa.get_url_value("back_login_url")
        self.user_account = self.pa.get_user_account()
        self.username_path = self.pa.get_emelent_path("back_username")
        self.password_path = self.pa.get_emelent_path("back_password")
        self.verify_path = self.pa.get_emelent_path("verify_code")
        self.button_path = self.pa.get_emelent_path("confirm_button")
        self.factory_path = self.pa.get_emelent_path("factory_path")
        self.components_path = self.pa.get_emelent_path("components_button")
        self.components_addpath = self.pa.get_emelent_path("components_add_button")
        self.image_button = self.pa.get_emelent_path("image_button")
        self.comName_input = self.pa.get_emelent_path("comName_input")
        self.comNumb_input = self.pa.get_emelent_path("comNumb_input")
        self.comComfire = self.pa.get_emelent_path("components_confirm")
        self.comNumb_check = self.pa.get_emelent_path("check_comNumb")
        self.comNanme_check = self.pa.get_emelent_path("check_comName")

    def test01_addcomponents(self):
        driver = self.driver
        lo = Login_Page(driver)
        comp = Components(driver)
        lo.login_url(self.url)
        #登录操作
        lo.login_input(self.username_path, self.user_account[0],
                       self.password_path, self.user_account[1],
                       self.verify_path, "6666",
                       self.button_path)
        time.sleep(1)
        comp.click_factory(self.factory_path)
        time.sleep(1)
        comp.click_components(self.components_path)
        time.sleep(1)
        # 点击内置零部件页面的添加按钮
        comp.add_button(self.components_addpath)
        time.sleep(1)
        # 填入随机生成的零部件名称
        comName = ''.join(random.sample([chr(i) for i in range(97, 123)], 5))
        comp.input_components_name(self.comName_input, comName)
        # 填入随机生成的5位型号值
        comNumb = "".join(random.choices([str(i) for i in range(0, 10)], k=5))
        comp.input_model_number(self.comNumb_input, comNumb)
        # 点击图片上传按钮
        comp.click_imagebutton(self.image_button)
        time.sleep(1)
        # 获取Script目录中上传脚本的绝对路径
        scriptdir = os.path.abspath(os.path.join(os.getcwd(), "../..")) + r"\Script\upload.exe"
        # 执行上传脚本
        os.system(scriptdir)
        time.sleep(2)
        comp.click_button(self.comComfire)
        time.sleep(1)
        # 获取添加后第一条数据的名称（第一天数据默认展示最新添加的项）
        checkName = comp.comName_check(self.comNanme_check)
        # 获取添加后第一天数据的型号
        checkNum = comp.comNumb_check(self.comNumb_check)
        flag = False
        #与随机生成的作比较，进行断言
        if checkNum == comNumb and checkName == comName:
            flag = True
        self.assertTrue(flag)
