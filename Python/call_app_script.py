#=========================================================------
#***PURPOSE***
#-------------
# Handle an API request to call a google apps script that can manage actions such as 
# connecting a google form's responses to a google sheet
# 
#

import os
import pickle
import requests
import google.auth
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

WEB_APP_URL = "https://script.google.com/macros/s/AKfycbzu6eLbKVl-fEMbXb4Tn-gZG3Xjseg8BpuHi8gFtIOzhh6YNPYQBbVyM6sCZUSgfPfwyQ/exec" 
#Comes from the deploy section in the google app script we run

SCOPES = ['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/script.external_request', 'https://www.googleapis.com/auth/script.scriptapp', 'https://www.googleapis.com/auth/forms', 'https://www.googleapis.com/auth/spreadsheets']  
#Spreadsheets and forms scopes are required by the app script. Drive scope seemed to fix an authentication 401 error. The other two may or may not be necessary for calling app scripts, I'm not sure.

def authenticate_google_account():
    '''
    Accesses or creates a token and initiates OAuth flow if necessary. Returns the credentials.
    '''
    creds = None
    #If we already have a token, go ahead and use that
    if os.path.exists('token.pickle'): 
        print("Token exists")
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
        if not creds.valid:
            print("Credentials are not currently valid")

    #If the token doesnt exist or needs to be refreshed, lets do that
    if not creds or not creds.valid: 
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            #The 'flow' will open in the browser and request you to select an account and approve the app to manage it
            flow = InstalledAppFlow.from_client_secrets_file(
                'api_data/credentials.json', SCOPES)
            creds = flow.run_local_server(port=8080) #originally 0, a dynamically chosen port, but set now to specific so the API can work

        #Save the new token in the .pickle file
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    
    return creds

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

def clear_token():
    '''
    Attempts to clear the current token by revoking it and deleting the file
    '''
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
        revoke_token(creds.token)

def revoke_token(token):
    '''
    Attempts to revoke the inputted token
    '''
    url = f'https://oauth2.googleapis.com/revoke?token={token}'
    response = requests.post(url)
    
    if response.status_code == 200:
        print("Token successfully revoked.")
        if os.path.exists('token.pickle'):
            os.remove('token.pickle')
            print("Token file deleted.")
    else:
        print(f"Failed to revoke token. Status code: {response.status_code}")

if __name__ == '__main__':
    pass
    #My test call that successfully linked a form to a specific google sheet
    #params = {'function': 'linkFormToSheet', 'f_id': '17PoKFAum28Fd_WdggV5QUOUnJvcuMh_9U36MZcP2ncQ', 's_id': '1JQ6Qm55Ku-jQoNn9mDhxVUzCb8dE-Sk2oZ7x4hF1diI'}
    #call_google_apps_script(params)
