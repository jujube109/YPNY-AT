class Page():
    def __init__(self,driver):
        self.driver=driver
    def clicktopica(self,topica_path):
        self.driver.find_element_by_xpath(topica_path).click()
    def click_sim(self,sim_path):
        self.driver.find_element_by_xpath(sim_path).click()
    def click_collection_address(self,collection_path):
        self.driver.find_element_by_xpath(collection_path).click()
    def click_factory(self,factory_path):
        self.driver.find_element_by_xpath(factory_path).click()
    def click_components(self,components_path):
        self.driver.find_element_by_xpath(components_path).click()
