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

