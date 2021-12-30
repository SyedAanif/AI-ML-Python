import requests
import json
url="http://localhost:8111/api"
data=json.dumps({'sl':3.2,'sw':7.3,'pl':4.5,'pw':2.1})
r=requests.post(url,data)
print(r.json())
