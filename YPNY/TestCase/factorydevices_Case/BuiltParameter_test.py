import unittest

from selenium.common.exceptions import ElementNotInteractableException
from lib.Parametric import Get_Parametric
from page.login_page import Login_Page
from selenium import webdriver
from page.devices_parameter import BuiltParameter
from selenium.webdriver.common.by import By
import random


class BulitParameterTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.lb = Get_Parametric()
        self.url = self.lb.get_url_value("back_login_url")
        self.user_account = self.lb.get_user_account()
        self.factory_path = self.lb.get_emelent_path("factory_path")
        self.BP_button = self.lb.get_emelent_path("BP_button")
        self.BP_addbuttion = self.lb.get_emelent_path("BP_addButton")
        self.BP_addwaitpath = self.lb.get_emelent_path("BP_addwaitpath")
        self.BP_clicksgin = self.lb.get_emelent_path("BP_clicksign")
        self.BP_selectcalcsign = self.lb.get_emelent_path("BP_alarmsignli")
        self.BP_thresholdpath = self.lb.get_emelent_path("BP_InputAlarmThreshold")
        self.BP_clicklevel = self.lb.get_emelent_path("BP_clicklevel")
        self.BP_choicelevel = self.lb.get_emelent_path("BP_alarmlevelli")
        self.BP_alarmconfirm = self.lb.get_emelent_path("BP_alarmconfirm")
        self.alertinfo = self.lb.get_emelent_path("BP_alertinfo")

    # 添加内置设备参数
    def test01_addparatemer(self):

        self.BP_inputname = self.lb.get_emelent_path("BP_NameInput")
        self.BP_inputtype = self.lb.get_emelent_path("BP_TypeInput")
        self.BP_lipath = self.lb.get_emelent_path("BP_lipath")
        self.BP_typetextJS = self.lb.get_emelent_path("BP_typetxtJS")
        self.BP_unittextJS = self.lb.get_emelent_path("BP_unitJS")
        self.BP_dataInput = self.lb.get_emelent_path("BP_dataID_input")
        self.BP_confirmbutton = self.lb.get_emelent_path("BP_confirm")
        self.BP_alarmRuleText = self.lb.get_emelent_path("BP_alarmRuleText")
        self.BP_checkname = self.lb.get_emelent_path("BP_checkName")
        driver = self.driver
        login = Login_Page(driver)
        BP = BuiltParameter(driver)

        login.login_url(self.url)
        login.login(self.user_account[0], self.user_account[1], "6666", )

        BP.wait((By.XPATH, self.factory_path))
        BP.click_factory(self.factory_path)
        BP.wait((By.XPATH, self.BP_button))
        BP.click_BuiltParameter(self.BP_button)
        BP.wait((By.CSS_SELECTOR, self.BP_addbuttion))
        BP.add_button(self.BP_addbuttion)
        name = "测试参数" + str(random.randint(0, 1000))
        BP.input_ParameterName(self.BP_inputname, name)
        try:
            BP.choice_ParameterType(self.BP_inputtype, self.BP_lipath)
        except ElementNotInteractableException as msg:
            print("Li元素查找异常%s" % msg)
        typetxt = BP.get_ParameterTypeText(self.BP_typetextJS)
        unittype = BP.get_Unit(self.BP_unittextJS)
        flag: bool = False
        if typetxt == "压力":
            if unittype == "KPa" or unittype == "MPa":
                flag = True
        elif typetxt == "温度":
            if unittype == "℃":
                flag = True
        elif typetxt == "液位高度":
            if unittype == "mm":
                flag = True
        elif typetxt == "次数":
            if unittype == "次":
                flag = True
        elif typetxt == "累计时间":
            if unittype == "天":
                flag = True
        elif typetxt == "累计方量":
            if unittype == "m³":
                flag = True
        elif typetxt == "频率":
            if unittype == "Hz":
                flag = True
        elif typetxt == "电流":
            if unittype == "A" or unittype == "mA":
                flag = True
        elif typetxt == "状态":
            if unittype == "--":
                flag = True
        BP.input_dataID(self.BP_dataInput, "01")
        self.assertTrue(flag)
        BP.click_confirm(self.BP_confirmbutton)
        BP.wait((By.XPATH, self.BP_alarmRuleText))
        checkname = BP.check_name(self.BP_checkname)
        self.assertEqual(name, checkname)

    # 规则页面添加报警规则
    def test02_alarmrule_add(self):
        driver = self.driver
        login = Login_Page(driver)
        BP = BuiltParameter(driver)
        self.BP_alarmbutton = self.lb.get_emelent_path("BP_alarmbutton")
        self.BP_alarmname = self.lb.get_emelent_path("BP_alarmname")
        self.BP_alarmaddbutton = self.lb.get_emelent_path("BP_alarm-add-button")
        self.BP_inputrulename = self.lb.get_emelent_path("BP_inputrulename")
        self.checkalarmname = self.lb.get_emelent_path("BP_checkname")
        login.login_url(self.url)
        login.login(self.user_account[0], self.user_account[1], "6666", )
        BP.wait((By.XPATH, self.factory_path))
        BP.click_factory(self.factory_path)
        BP.wait((By.XPATH, self.BP_button))
        BP.click_BuiltParameter(self.BP_button)
        BP.wait((By.XPATH, self.BP_alarmbutton))
        BP.click_alarmRule(self.BP_alarmbutton)
        BP.add_button(self.BP_alarmaddbutton)
        BP.wait((By.CSS_SELECTOR, self.BP_addwaitpath))
        self.alarmname = "测试报警规则" + str(random.randint(0, 100))
        BP.input_rulename(self.BP_inputrulename, self.alarmname)
        # 随机选择运算符号
        BP.choice_calc_sign(self.BP_clicksgin, self.BP_selectcalcsign)
        # 输入随机阈值
        self.thresholdvalue = random.randint(0, 100)
        BP.wati_disappear((By.XPATH, "//span[text()='>']/parent::li/parent::ul"))
        BP.input_threshold(self.BP_thresholdpath, self.thresholdvalue)
        # 随机选择报警等级
        BP.choice_level(self.BP_clicklevel)
        # 点击确认按钮
        BP.click_alarmconfire(self.BP_alarmconfirm)
        BP.wait((By.XPATH, self.alertinfo))
        checkname = BP.get_alarmname(self.checkalarmname)
        self.assertEqual(checkname, self.alarmname)

    # 参数列表页面列项添加报警规则,并为第一条参数增加报警规则
    def test03_addalarmfromBPpage(self):
        driver = self.driver
        login = Login_Page(driver)
        BP = BuiltParameter(driver)
        self.BP_Palarmbutton = self.lb.get_emelent_path("BP_Paddalarmbutton")
        self.BP_PItemaddalarmbutton = self.lb.get_emelent_path("BP_PItemaddalarmbutton")
        self.BP_PItemInput = self.lb.get_emelent_path("BP_PItemInput")
        self.BP_Palarmconfirm = self.lb.get_emelent_path("BP_Palarmconfirm")
        self.BP_selectalarm = self.lb.get_emelent_path("BP_select_to_selected")
        self.BP_selectalarmconfirm = self.lb.get_emelent_path("BP_selectAlarmConfirm")
        self.BP_selectSuccessAlert = self.lb.get_emelent_path("BP_selectSuccessAlert")
        login.login_url(self.url)
        login.login(self.user_account[0], self.user_account[1], "6666", )
        BP.wait((By.XPATH, self.factory_path))
        BP.click_factory(self.factory_path)
        BP.wait((By.XPATH, self.BP_button))
        BP.click_BuiltParameter(self.BP_button)
        BP.wait((By.CSS_SELECTOR, self.BP_addbuttion))
        BP.click_Palarmbutton(self.BP_Palarmbutton)
        BP.wait((By.XPATH, self.BP_Palarmbutton))
        BP.click(self.BP_PItemaddalarmbutton)
        BP.wait((By.CSS_SELECTOR, self.BP_addwaitpath))
        ruleName = "参数页面添加报警规则" + str(random.randint(0, 100))
        BP.sendkeys(ruleName)
        BP.choice_calc_sign(self.BP_clicksgin, self.BP_selectcalcsign)
        self.thresholdvalue = random.randint(0, 100)
        BP.input_threshold(self.BP_thresholdpath, self.thresholdvalue)
        # 随机选择报警等级
        BP.choice_level(self.BP_clicklevel)
        BP.click(self.BP_Palarmconfirm)
        BP.wait((By.XPATH, self.alertinfo))
        check_name = BP.get_Pcheckname()
        self.assertIn(ruleName, check_name)
        BP.select_alarmrule()
        BP.click(self.BP_selectalarm)
        BP.wait((By.XPATH, self.alertinfo))
        BP.click(self.BP_selectalarmconfirm)
        BP.wait((By.XPATH, self.BP_selectSuccessAlert))
        text = BP.get_alertText()
        self.assertEqual("添加报警规则：成功", text)


    def tearDown(self):
        self.driver.close()
