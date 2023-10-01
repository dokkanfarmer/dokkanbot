import snowmate_collector
import pathlib
snowmate_collector.start(
    project_path=str(pathlib.Path("/home/oni/dokkan bot repo")),  
    project_id="651594d37fd78c9fb3eac42a",
    client_id="4ec2b424-c87b-41c0-9a7a-b554eeea00d6",
    secret_key="59148ead-dd9b-4327-822e-e156f0564a5b",
)
import requests
import base64

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def login(license_key):
	r=requests.post(base64.b64decode('aHR0cHM6Ly92aXAuZGJ6ZGIucHcv'),data={'license':license_key})
	return 'Welcome ' in r.content
	
if __name__ == "__main__":
	license=input('your license key: ')
	if len(license)!=32:
		print ('invalid license, you can buy one here placeholder/')
		exit(1)
	if login(license):
		print ('you can now use the bot :)')
	else:
		print ('invalid license, you can buy one here placeholder/')


