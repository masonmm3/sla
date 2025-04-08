#=========================================================------
#***PURPOSE***
#-------------
# Handle an API request to call a google apps script that can manage actions such as 
# connecting a google form's responses to a google sheet
# 

import requests
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from authentication import authenticate_google_account

WEB_APP_URL = "https://script.google.com/macros/s/AKfycbzu6eLbKVl-fEMbXb4Tn-gZG3Xjseg8BpuHi8gFtIOzhh6YNPYQBbVyM6sCZUSgfPfwyQ/exec" 
#Comes from the deploy section in the google app script we run

SCOPES = ['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/script.external_request', 'https://www.googleapis.com/auth/script.scriptapp', 'https://www.googleapis.com/auth/forms', 'https://www.googleapis.com/auth/spreadsheets']  
#Spreadsheets and forms scopes are required by the app script. Drive scope seemed to fix an authentication 401 error. The other two may or may not be necessary for calling app scripts, I'm not sure.


def call_google_apps_script(params):
    '''
    Attempts calling the google apps script file from WEB_APP_URL with the inputted parameters
    '''
    creds = authenticate_google_account()

    headers = {
        'Authorization': f'Bearer {creds.token}'
    }

    #The API request is made here, using the web app url (determining which script to run), 
    #the parameters (determining which function to run), and token (inside of headers)
    response = requests.get(url=WEB_APP_URL,params=params, headers=headers)

    if response.status_code == 200:
        print("Google Apps Script executed successfully!")
        print(response.text)
    else:
        print(f"Failed to execute script. Status code: {response.status_code}")
        print(response.text)

if __name__ == '__main__':
    pass
    #My test call that successfully linked a form to a specific google sheet
    #params = {'function': 'linkFormToSheet', 'f_id': '17PoKFAum28Fd_WdggV5QUOUnJvcuMh_9U36MZcP2ncQ', 's_id': '1JQ6Qm55Ku-jQoNn9mDhxVUzCb8dE-Sk2oZ7x4hF1diI'}
    #call_google_apps_script(params)
