from  page.page import Page
import time
import random
class SimAddPage(Page):
    def simAddButton(self,sim_add_button):
        self.driver.find_element_by_xpath(sim_add_button).click()
    def ispChoice(self,isplist_buttonpath,isps_textpath):
        self.driver.find_element_by_xpath(isplist_buttonpath).click()
        time.sleep(1)
        isplist=self.driver.find_elements_by_xpath(isps_textpath)
        choice_isp=random.choice(isplist)
        isp_text=choice_isp.text
        choice_isp.click()
        return isp_text
    def simOwner(self,owner_inputpath,vaule):
        self.driver.find_element_by_xpath(owner_inputpath).send_keys(vaule)
    def phoneNum(self,phonenumber_path,value):
        self.driver.find_element_by_xpath(phonenumber_path).send_keys(value)
    def confirm(self,confirmbutton_path):
        self.driver.find_element_by_xpath(confirmbutton_path).click()
    def checkOwner(self,checkOwner_path):
        text=self.driver.find_element_by_xpath(checkOwner_path).text
        return text
    def checkIsm(self,checkIsm_path):
        text = self.driver.find_element_by_xpath(checkIsm_path).text
        return text