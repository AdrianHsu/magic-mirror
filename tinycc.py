import requests
import json

url='http://stackoverflow.com/questions/25016301/class-requests-models-response-to-json'

query_params = {'apiKey': '9e19998c-0097-4058-957c-0e663537c44c',
				'login': 'ryan2448',
                'longUrl': '?'} 
endpoint = 'http://tiny.cc/?c=rest_api&m=shorten&version=2.0.3'

response = requests.get(endpoint, params=query_params, verify=False)
print(response)
data = json.loads(response.text)
print(data)