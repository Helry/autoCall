
import requests
import time

url = 'http://ecall2.huaqiweb.com/ecall/api/callback'

AgentID = '98'
apppackage = 'com.social-call.app'
pwd = 'bbe1c44eb91fcd44a7693e7cba7c7103'
to = '13413093405'
userId = '82092'

data = {
    'AgentID':AgentID,
    'apppackage':apppackage,
    'pwd':pwd,
    'to':to,
    'userId':userId
}

times = 1
# begin 
for _ in range(times):
	# request call api 
	requests.post(url=url,data=data)
	# debug 
	print(requests.post(url=url,data=data).text)
	# delay 10S 
	time.sleep(10)
    
