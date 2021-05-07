from page.page import Page


class CollectionPage(Page):
    def collectionAddButton(self, addbutton_path):
        self.driver.find_element_by_css_selector(addbutton_path).click()
    def input_DataID(self,path,value):
        self.driver.find_element_by_xpath(path).send_keys(value)
    def input_Address(self,path,value):
        self.driver.find_element_by_xpath(path).send_keys(value)
    def confirm(self,confirmbutton_path):
        self.driver.find_element_by_css_selector(confirmbutton_path).click()
    def dataText(self,path):
        return self.driver.find_element_by_xpath(path).text
    def addressText(self,path):
        return self.driver.find_element_by_xpath(path).text