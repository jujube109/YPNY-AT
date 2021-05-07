from  page.page import  Page

class Components(Page):
    def add_button(self,path):
        self.driver.find_element_by_xpath(path).click()
    def click_imagebutton(self,path):
        self.driver.find_element_by_xpath(path).click()
    def input_components_name(self,path,name):
        self.driver.find_element_by_xpath(path).send_keys(name)
    def input_model_number(self,path,number):
        self.driver.find_element_by_xpath(path).send_keys(number)
    def click_button(self,path):
        self.driver.find_element_by_xpath(path).click()
    def comName_check(self,path):
        text= self.driver.find_element_by_xpath(path).text
        return text
    def comNumb_check(self,path):
        text=self.driver.find_element_by_xpath(path).text
        return text