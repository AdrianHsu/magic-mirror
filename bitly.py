import requests
import json

query_params = {'access_token': '763e313dc7f60f693de1dbbe04bad650728d899a',
                'longUrl': 'http://stackoverflow.com/questions/25016301/class-requests-models-response-to-json'} 

endpoint = 'https://api-ssl.bitly.com/v3/shorten'
response = requests.get(endpoint, params=query_params, verify=False)

data = json.loads(response.text)
print(data['data']['url'])