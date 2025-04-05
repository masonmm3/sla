#=========================================================------
#***PURPOSE***
#-------------
# Update "program_data.json" to include new program details when
# an SLA employee enters information into the program creation form
#
#***Data required***
#-------------------
# The URL of the creation form to check

import json
import numpy as np
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from authentication import authenticate_google_account

CREATION_FORM_ID = "1GCE8SIKYwvZ8YNni_V0cHsCPmJD9pfps2NY1AjdBOJg"
#Id to the sheet that receives responses from the SLA Program Creation form

SCOPES = ['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/forms', 'https://www.googleapis.com/auth/spreadsheets']  
#Permissions we request

def get_range(spreadsheet_id, range_name):
    '''
    Retrieves a range from any spreadsheet
    Returns a result which you can access values from with .get("values", [])
    '''
    creds = authenticate_google_account(SCOPES)
    # pylint: disable=maybe-no-member

    try:
        service = build("sheets", "v4", credentials=creds)

        result = (
            service.spreadsheets()
            .values()
            .get(spreadsheetId=spreadsheet_id, range=range_name)
            .execute()
        )
        rows = result.get("values", [])
        print(f"{len(rows)} rows retrieved")
        return result
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error
    
def read_new_rows(spreadsheet_id):
    #Get the file containg latest_row and read the value off it
    with open("creation_data.json", "r") as f:
        creation_data = json.load(f)
        latest_row = int(creation_data.get("latest_row"))
        if latest_row <= 1:
            latest_row = 2
        
    #Set the range to any new rows and get the values from this range
    range_string = "A"+str(latest_row)+":D"
    result = get_range(spreadsheet_id, range_string)
    values = result.get("values", [])

    #Get the number of rows just discovered and increase latest_row accordingly
    num_rows = len(values)
    latest_row += num_rows
    
    #Update the file containing latest_row
    with open("creation_data.json", "w") as f:
        creation_data["latest_row"] = latest_row
        json.dump(creation_data, f, indent=4)

    return values

if __name__ == "__main__":
  values = read_new_rows(CREATION_FORM_ID)
  print(values)