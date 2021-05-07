from locust import TaskSet,task,HttpUser
import hashlib
import json
import  requests

token = "faliure"

class UserBehavior(TaskSet):

    @staticmethod
    def login():
        pw = '123456'
        md = hashlib.md5()
        md.update(pw.encode('utf-8'))
        pwd5 = md.hexdigest()
        url = "http://192.168.0.110:8961/login/login"
        payload = json.dumps({
            "code": "6666",
            "password": pwd5,
            "username": "jujube109"
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request('post',url, headers=headers, data=payload)
        return response.headers['x-auth-token']
    @task(2)
    def alarm(self):
        global token
        #print("token=={0}".format(token))
        body={
            "asc": True,
            "current": 0,
            "keyword": "",
            "orderByFields": [
                "createTime"
            ],
            "siteEquipmentParameterId": 0,
            "size": 0,
            "stationId": 0
        }
        #token = self.login()
        head={
            'x-auth-token': token,
            'Content-Type': 'application/json'
        }
        with self.client.post("/siteAlarmRule/records",headers= head,json=body,catch_response = True) as response:
            code=response.json().get("code")
            key=response.json().get("key")
            request_header=response.request.headers
            request_token=dict(request_header).get("x-auth-token")
            print("{0}--->:{1}\n--token:{2}".format(key,request_header,request_token),end="\n")
            if key == "NOT_LOGIN":
                token = self.login()
            if request_token == "faliure": #首次token值为随意输入的字符串，所以会有一个失败请求手动打成成功，用于触发上一个IF条件，获取新token达到所有请求使用一个token
                #response.success()
                response.failure("首次登录无效token")
                return 0
            if code != 200 and key!= "SUCCESS":
                response.failure("未成功请求响应码:%dkey值:%s"%(code,key))
    @task(1)
    def get_pa(self):
        global token
        head = {
            'x-auth-token': token,
            'Content-Type': 'application/json'
        }

        with self.client.get("/equipment/monitor/stationId/154976270691840000",headers=head,catch_response = True) as response:
            code=response.json().get("code")
            key=response.json().get("key")
            request_header=response.request.headers
            request_token=dict(request_header).get("x-auth-token")
            print("eeee{0}--->:{1}\n--token:{2}".format(key,request_header,request_token),end="\n")
            if key == "NOT_LOGIN":
                token = self.login()
            if request_token == "faliure": #首次token值为随意输入的字符串，所以会有一个失败请求手动打成成功，用于触发上一个IF条件，获取新token达到所有请求使用一个token
                #response.success()
                response.failure("首次登录无效token")
                return 0
            if code != 200 and key!= "SUCCESS":
                response.failure("未成功请求响应码:%dkey值:%s"%(code,key))

class WebsiteUser(HttpUser):
    tasks =[UserBehavior]
    min_wait = 1000
    max_wait = 9000
    host = 'http://192.168.0.110:8961'

