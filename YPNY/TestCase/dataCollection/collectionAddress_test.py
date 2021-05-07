import unittest
from selenium import webdriver
from page.data_collection import CollectionPage
from lib.Parametric import Get_Parametric
from page.login_page import Login_Page
from lib.phonenumber import PhoneNum
import time


class CollectionAddress(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.pa = Get_Parametric()
        self.topic_path = self.pa.get_emelent_path("topica_path")
        self.collection_path = self.pa.get_emelent_path("collection_path")
        self.collectionAdd_path = self.pa.get_emelent_path("collection_add_button")
        self.url = self.pa.get_url_value("back_login_url")
        self.user_account = self.pa.get_user_account()
        self.username_path = self.pa.get_emelent_path("back_username")
        self.password_path = self.pa.get_emelent_path("back_password")
        self.verify_path = self.pa.get_emelent_path("verify_code")
        self.button_path = self.pa.get_emelent_path("confirm_button")
        self.dataid_inputpath = self.pa.get_emelent_path("dataid_inputpath")
        self.collection_inputpath = self.pa.get_emelent_path("collection_inputpath")
        self.confirm_buttonpath = self.pa.get_emelent_path("collection_confirmpath")
        self.datatext_patth = self.pa.get_emelent_path("datatext_path")
        self.addresstext_path = self.pa.get_emelent_path("addresstext_path")

    def test01_success_add(self):
        driver = self.driver
        lo = Login_Page(driver)
        lo.login_url(self.url)
        lo.login_input(self.username_path, self.user_account[0],
                       self.password_path, self.user_account[1],
                       self.verify_path, "6666",
                       self.button_path)
        time.sleep(1)
        lo.clicktopica(self.topic_path)
        time.sleep(1)
        lo.click_collection_address(self.collection_path)
        time.sleep(1)
        collection = CollectionPage(driver)
        collection.collectionAddButton(self.collectionAdd_path)
        time.sleep(1)
        dataId = PhoneNum().dataId()  # 获取随机的dataId
        collection.input_DataID(self.dataid_inputpath, dataId)
        address = PhoneNum().address()
        collection.input_Address(self.collection_inputpath, address)
        collection.confirm(self.confirm_buttonpath)
        time.sleep(1)
        dataIdtext = collection.dataText(self.datatext_patth)
        addresstext = collection.addressText(self.addresstext_path)
        print(dataIdtext, addresstext)
        flag = False
        if dataIdtext == dataId and addresstext == address:
            flag = True
        self.assertTrue(flag)
