import requests
import json
import sys
import time

infile=open(sys.argv[1],"r")
inlines=infile.readlines()

outfile=open("twistOut.txt", "a")

for line in inlines:
        line=line.replace('\n', '')
        line=line.replace('\r', '')
        print("===== working on domain"+ line +" =====")
        domain=line
        domain=domain.encode().hex()
        x=requests.get('https://dnstwister.report/api/fuzz/'+domain)
        statuscode=x.status_code
        if statuscode==200:
                response=x.content
                response=response.decode('utf-8')
                response=json.loads(response)

                fuzz_array=response['fuzzy_domains']

                for item in fuzz_array:
                        print(item['domain'])
                        outfile.write(item['domain']+"\n")
        else:
                print("statuscode for"+line+"is"+str(statuscode))
        time.sleep(3)

outfile.close()
