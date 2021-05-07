import os
import json
import random


class Get_Parametric:
    def __init__(self):
     self.current_path=os.path.dirname(__file__)
    def get_url_value(self,value):
        keyword = value
        with open(self.current_path + "/data.json", "r",encoding="utf-8") as data_file:
            #打开data文件，获取约定好的url字典中的所有数据，再通过传入的value，获取指定的数据，’url‘与value值均可在data文件中配置
            #用例代码中调用时只，需要传入data文件中url下对应的key值
            url_json = json.load(data_file)
            all_url=url_json['url']
            need_url=all_url[keyword]
            data_file.close()
            return need_url
            #return url_json['url'][keyword]
    def get_emelent_path(self,pathname):
        keyword=pathname
        with open(self.current_path+"/data.json", "r",encoding="utf-8") as data_file:
            element_json = json.load(data_file)
            all_element = element_json['element-path']
            need_element = all_element[keyword]
            data_file.close()
            return need_element

    def get_user_account(self):
        all_user= list()
        with open(self.current_path + "/data.json", "r",encoding="utf-8") as data_file:
            user_json = json.load(data_file)
            all_account = user_json['user-account']
            for key in all_account.items():
                all_user.append(key)
            data_file.close()
        selected_user=random.choice(all_user)
        return  selected_user
