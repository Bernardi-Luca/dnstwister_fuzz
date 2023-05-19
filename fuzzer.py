import requests
import json

domain='aaa.com'

domain=domain.encode().hex()

x=requests.get('https://dnstwister.report/api/fuzz/'+domain)

response=x.content

response=response.decode('utf-8')

response = json.loads(response)

fuzz_array=response['fuzzy_domains']

for item in fuzz_array:
        print(item['domain'])
