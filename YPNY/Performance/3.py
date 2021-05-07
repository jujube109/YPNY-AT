from locust import TaskSet,HttpLocust,task,HttpUser
import hashlib
import json
import  requests



def login():
    pw = '123456'
    md = hashlib.md5()
    md.update(pw.encode('utf-8'))
    pwd5 = md.hexdigest()
    url = "http://192.168.0.110:8961/login/login"
    payload = json.dumps({
        "code": "6666",
        "password": pwd5,
        "username": "admin"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    s = requests.Session()
    response = s.post(url, headers=headers, data=payload)
    return response.headers['x-auth-token']

class UserBehavior2(TaskSet):
    @task(1)
    def get_pa(self):
        token = login()
        head = {
            'x-auth-token': token,
            'Content-Type': 'application/json'
        }

        r=self.client.get("/equipment/monitor/stationId/154976270691840000",headers=head)
        print(type(r.text))
class WebsiteUser(HttpUser):
    tasks =[UserBehavior2]
    min_wait = 1000
    max_wait = 9000