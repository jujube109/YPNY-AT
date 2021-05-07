from page.login_page import Login_Page
from selenium import webdriver
import unittest
from lib.Parametric import Get_Parametric
import time


class LoginTest(unittest.TestCase):
    # 登录功能所有的用例均在此类中实现
    """
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()

        cls.pa = Get_Parametric()
        cls.url = cls.pa.get_url_value("back_login_url")
        cls.user_account = cls.pa.get_user_account()
        cls.username_path = cls.pa.get_emelent_path("back_username")
        cls.password_path = cls.pa.get_emelent_path("back_password")
        cls.verify_path = cls.pa.get_emelent_path("verify_code")
        cls.button_path = cls.pa.get_emelent_path("confirm_button")
    """

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.pa = Get_Parametric()
        self.lg = Login_Page(self.driver)
        self.url = self.pa.get_url_value("back_login_url")
        self.user_account = self.pa.get_user_account()
        self.username_path = self.pa.get_emelent_path("back_username")
        self.password_path = self.pa.get_emelent_path("back_password")
        self.verify_path = self.pa.get_emelent_path("verify_code")
        self.button_path = self.pa.get_emelent_path("confirm_button")

    def test01_success_login(self):
        # 返回用户名密码的元组对象，索引0为用户名，索引1为密码

        self.lg.login_url(self.url)
        self.lg.login_input(self.username_path, self.user_account[0],
                            self.password_path, self.user_account[1],
                            self.verify_path, "6666",
                            self.button_path)
        time.sleep(1)
        assert_text = self.driver.find_element_by_xpath(self.pa.get_emelent_path("assert_success_login")).text
        self.assertEqual(assert_text, "工艺图")

    def test02_no_username(self):
        user_account = self.pa.get_user_account()
        self.lg.login_url(self.url)
        self.lg.login_input(self.username_path, '',
                            self.password_path, user_account[1],
                            self.verify_path, "6666",
                            self.button_path)
        erro_text = self.driver.find_element_by_xpath(self.pa.get_emelent_path("username_erro_information")).text
        self.assertEqual(erro_text, "请输入用户名")

    def test03_no_password(self):
        user_account = self.pa.get_user_account()
        self.lg.login_url(self.url)
        self.lg.login_input(self.username_path, user_account[0],
                            self.password_path, '',
                            self.verify_path, "6666",
                            self.button_path)
        erro_text = self.driver.find_element_by_xpath(self.pa.get_emelent_path("password_erro_information")).text
        self.assertEqual(erro_text, "密码必填")
    def test04_no_verify(self):
        user_account = self.pa.get_user_account()
        self.lg.login_url(self.url)
        self.lg.login_input(self.username_path, user_account[0],
                            self.password_path, user_account[1],
                            self.verify_path, "",
                            self.button_path)
        time.sleep(1)
        erro_text = self.driver.find_element_by_xpath(self.pa.get_emelent_path("verify_erro_information")).text
        self.assertEqual(erro_text,"请输入验证码")
    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()
