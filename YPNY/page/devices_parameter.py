from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, \
    ElementClickInterceptedException
from lib.Parametric import Get_Parametric
from page.page import Page
from selenium.webdriver.common.by import By
import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

lb = Get_Parametric()
class BuiltParameter(Page):


    # 点击添加按钮
    def add_button(self, path):
        self.driver.find_element_by_css_selector(path).click()

    # 输入参数名称
    def input_ParameterName(self, path, name):
        self.driver.find_element_by_xpath(path).send_keys(name)

    # 随机选择参数类型，且获取随机点击类型的文本
    def choice_ParameterType(self, path, lipath):
        self.driver.find_element_by_xpath(path).click()
        #等待元素可点击
        self.wait((By.XPATH, "//span[text()='频率']/parent::li"))
        typelists = self.driver.find_elements_by_xpath(lipath)
        selectedtype = random.choice(typelists)
        try:
            selectedtype.click()
        except ElementNotInteractableException:
            action = ActionChains(self.driver)
            action.move_to_element(selectedtype).perform()
            selectedtype.click()
        except ElementClickInterceptedException:
            action = ActionChains(self.driver)
            action.move_to_element(selectedtype).perform()
            selectedtype.click()

    # 获取所选参数的文本，用于匹配自动补全的单位判断断言
    def get_ParameterTypeText(self, typejs):
        typetext = self.driver.execute_script(typejs)
        return typetext

    # 获取自动带出的单位
    def get_Unit(self, unitjs):
        unittxt = self.driver.execute_script(unitjs)
        return unittxt

    # 输入dataID
    def input_dataID(self, path, value):
        self.driver.find_element_by_xpath(path).send_keys(value)

    # 点击添加页面的确认按钮
    def click_confirm(self, path):
        self.driver.find_element_by_xpath(path).click()

    # 获取添加后表格第一行第一列的参数名称
    def check_name(self, path):
        return self.driver.find_element_by_xpath(path).text

    # 点击顶端报警规则按钮进入报警规则页面
    def click_alarmRule(self, path):
        self.driver.find_element_by_xpath(path).click()

    # 点击规则添加按钮，套用点击参数添加的方法

    # 输入规则名
    def input_rulename(self, path, rulename):
        self.driver.find_element_by_xpath(path).send_keys(rulename)

    # 选择运算符号（随机选择一个）
    def choice_calc_sign(self, path, lipath):
        self.driver.find_element_by_xpath(path).click()
        self.wait((By.XPATH, "//span[text()='>']"))
        signslist = self.driver.find_elements_by_xpath(lipath)
        selectsign = random.choice(signslist)
        selectsign.click()

    # 输入阈值
    def input_threshold(self, path, value):
        self.driver.find_element_by_xpath(path).send_keys(value)

    # 随机选择告警等级
    def choice_level(self, path):
        lipath=lb.get_emelent_path("BP_Plevelli")
        self.driver.find_element_by_xpath(path).click()
        self.wait((By.XPATH, "//span[text()='低']"))
        levellist = self.driver.find_elements_by_xpath(lipath)
        selectlevel = random.choice(levellist)
        try:
            selectlevel.click()
        except ElementNotInteractableException:
            action = ActionChains(self.driver)
            action.move_to_element(selectlevel).perform()
            selectlevel.click()
        except ElementClickInterceptedException:
            action = ActionChains(self.driver)
            action.move_to_element(selectlevel).perform()
            selectlevel.click()
    # 点击确认按钮
    def click_alarmconfire(self, path):
        self.driver.find_element_by_css_selector(path).click()

    # 获取添加成功报警规则的规则名称
    def get_alarmname(self, path):
        return self.driver.find_element_by_xpath(path).text

    # 点击参数列表页面列项后面的报警规则
    def click_Palarmbutton(self, path):
        self.driver.find_element_by_xpath(path).click()

    # 通用点击方法
    def click(self, path):
        try:
            self.driver.find_element_by_css_selector(path).click()
        except NoSuchElementException:
            self.driver.find_element_by_xpath(path).click()

    # 通用输入传值
    def sendkeys(self, value):
        self.BP_PItemInput = lb.get_emelent_path("BP_PItemInput")
        try:
            self.driver.find_element_by_css_selector(self.BP_PItemInput).send_keys(value)
        except NoSuchElementException:
            self.driver.find_element_by_xpath(self.BP_PItemInput).send_keys(value)
    # 获取参数列表页添加的规则名
    def get_Pcheckname(self):
        self.BP_Pcheckname=lb.get_emelent_path("BP_Pcheckname")
        labellists=self.driver.find_elements_by_xpath(self.BP_Pcheckname)
        rule_name_text=labellists[len(labellists)-1].text
        return  rule_name_text
    def select_alarmrule(self):
        self.BP_Pcheckspan=lb.get_emelent_path("BP_Pselectbox")
        spanlists=self.driver.find_elements_by_xpath(self.BP_Pcheckname)
        spanlists[len(spanlists) - 1].click()

    def get_alertText(self):
        BP_selectSuccessAlert=lb.get_emelent_path("BP_selectSuccessAlert")
        alerttext=self.driver.find_element_by_xpath(BP_selectSuccessAlert).text
        return  alerttext

