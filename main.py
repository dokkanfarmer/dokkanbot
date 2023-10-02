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

# Disable SSL warnings (only if necessary)
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Function to perform the login operation
def login(license_key):
    return True
    
if __name__ == "__main__":
    license = input('Enter your license key: ')

if len(license) != 32:
     print('Invalid license. You can purchase one at: placeholder/')
     exit(1)

if login(license):
        print('You can now use the bot :)')
else:
    print('You can get a temporary key.')
    choice = input("1. Yes 2. No: ")

if choice == "1":
    pass
    login_url = base64.b64decode('aHR0cHM6Ly92aXAuZGJ6ZGIucHcv')
    response = requests.post(login_url, data={'license': license_key})
    return 'Welcome ' in response.content

if __name__ == "__main__":
    license = input('Enter your license key: ')

    if len(license) != 32:
        print('Invalid license. You can purchase one at: placeholder/')
        exit(1)

    if login(license):
        print('You can now use the bot :)')
    else:
        print('You can get a temporary key.')
        choice = input("1. Yes 2. No: ")

        if choice == "1":
            # Handle temporary key logic here
            pass


