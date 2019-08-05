#!/usr/bin/env python
import requests
import json
import cgi
import cgitb
import time
import pprint
import re

url='https://xxxx:9061/ins'
switchuser='x'
switchpassword=''
etherchannel = '104'
trunkervlan = '79'

myheaders={'content-type':'application/json-rpc'}
payload=[
{"jsonrpc": "2.0","method": "cli","params": {"cmd": "interface port-channel "+etherchannel,"version": 1},"id": 1},
{"jsonrpc": "2.0","method": "cli","params": {"cmd": "switchport trunk allowed vlan add "+trunkervlan,"version": 1},"id": 2},
{"jsonrpc": "2.0","method": "cli","params": {"cmd": "exit","version": 1},"id": 3}
]
response = requests.post(url,data=json.dumps(payload), headers=myheaders, verify=False, auth=(switchuser,switchpassword)).json()

print response

