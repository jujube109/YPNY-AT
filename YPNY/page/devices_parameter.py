from page.page import Page
from selenium.webdriver.common.by import By
import random
import time
class BuiltParameter(Page):
    def add_button(self,path):
        self.driver.find_element_by_css_selector(path).click()
    def input_ParameterName(self,path,name):
        self.driver.find_element_by_xpath(path).send_keys(name)
    def choice_ParameterType(self,path,lipath):
        self.driver.find_element_by_xpath(path).click()
        time.sleep(1)
        self.wait((By.XPATH,"//span[text()='压力']"))
        typelists=self.driver.find_elements_by_xpath(lipath)
        print(typelists)
        selectedType=random.choice(typelists)
        print(selectedType)
        selectedType.click()