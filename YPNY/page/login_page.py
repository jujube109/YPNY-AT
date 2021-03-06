from page.page import Page
from lib.Parametric import  Get_Parametric

lb = Get_Parametric()
username_path = lb.get_emelent_path("back_username")
password_path = lb.get_emelent_path("back_password")
verify_path = lb.get_emelent_path("verify_code")
button_path = lb.get_emelent_path("confirm_button")
user_account = lb.get_user_account()
class Login_Page(Page):

    def login_url(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(15)

    def input_username(self, username_path, user):
        username = self.driver.find_element_by_xpath(username_path)
        username.send_keys(user)

    def input_password(self, password_path, passwd):
        password = self.driver.find_element_by_xpath(password_path)
        password.send_keys(passwd)

    # 用于测试从所有用户中随机选择用户，功能是否生效
    def clear_username(self, username_path):
        username = self.driver.find_element_by_xpath(username_path)
        username.clear()

    def clear_password(self, password_path):
        password = self.driver.find_element_by_xpath(password_path)
        password.clear()

    def input_Verificationcode(self, code, code_path):
        verification_element = self.driver.find_element_by_xpath(code_path)
        verification_element.send_keys(code)

    def click_confirm(self, button_path):
        buttom_element = self.driver.find_element_by_xpath(button_path)
        buttom_element.click()


    def login_input(self,  user, password_path, passwd, code_path, code, button_path):
        username = self.driver.find_element_by_xpath(username_path)
        username.send_keys(user)
        password = self.driver.find_element_by_xpath(password_path)
        password.send_keys(passwd)
        verification_element = self.driver.find_element_by_xpath(code_path)
        verification_element.send_keys(code)
        buttom_element = self.driver.find_element_by_xpath(button_path)
        buttom_element.click()

    def login(self,user,passwd,code):
        username = self.driver.find_element_by_xpath(username_path)
        username.send_keys(user)
        password = self.driver.find_element_by_xpath(password_path)
        password.send_keys(passwd)
        verification_element = self.driver.find_element_by_xpath(verify_path)
        verification_element.send_keys(code)
        buttom_element = self.driver.find_element_by_xpath(button_path)
        buttom_element.click()