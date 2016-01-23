import os
import json
import requests

service_url = 'https://api.smooch.io'
app_token = os.environ['SMOOCH_APP_TOKEN']

payload = {
    'device': {
        'id': '7e6eedd677eb3ede0c636fc4c5b51a14',
        'platform': 'other'
    }
}
headers = {'content-type': 'application/json',
           'app-token': app_token}

res = requests.post(service_url + '/v1/init',
                    data=json.dumps(payload), headers=headers)

print res.status_code
print res.text
