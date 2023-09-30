import snowmate_collector
import pathlib
snowmate_collector.start(
    project_path=str(pathlib.Path("/home/oni/dokkan bot repo")),  
    project_id="651594d37fd78c9fb3eac42a",
    client_id="19bfe8b-e8c9-4ac3-8868-82c94eb502fc",
    secret_key="77e82f20-26b1-413a-b3cd-4c327bef5289",
)
import requests
import base64

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def login(license_key):
	r=requests.post(base64.b64decode('aHR0cHM6Ly92aXAuZGJ6ZGIucHcv'),data={'license':license_key})
	return 'Welcome ' in r.content
	
if __name__ == "__main__":
	license=raw_input('your license key: ')
	if len(license)<>32:
		print 'invalid license, you can buy one here placeholder/'
		exit(1)
	if login(license):
		print 'you can now use the bot :)'
	else:
		print 'invalid license, you can buy one here placeholder/'
