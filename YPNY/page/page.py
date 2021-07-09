from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page():
    def __init__(self,driver):
        self.driver=driver
    def wait(self, locator, timeout=10):
        """
        二次封装显式等待
        :param locator:
        :param timeout:
        :return:
        """
        WebDriverWait(self.driver, timeout). \
            until(EC.visibility_of_element_located(locator))
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
    def click_BuiltParameter(self,BP_path):
        self.driver.find_element_by_xpath(BP_path).click()
