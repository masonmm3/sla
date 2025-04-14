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

def perform_trigger():
    values, indices = read_new_rows()
    peform_actions(values, indices)

def get_sheet_range(spreadsheet_id, range_name):
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
    '''
    Checks for any new rows in the given spreadsheet and returns the values and the indexes in the gsheet of the new values
    '''

    #Set the range to all rows and get the values from this range
    range_string = "A2:E"
    result = get_sheet_range(spreadsheet_id, range_string)
    all_values = np.array(result.get("values", []))

    #Filter out to new rows
    completed_column = all_values[:, 0]
    values = [all_values[index, 1:].tolist() for index, val in enumerate(completed_column) if val != 'TRUE']
    index_list = [index for index, condition in enumerate(completed_column) if condition != 'TRUE']

    return values, index_list

def peform_actions(values, indices):
    '''
    Takes in all rows and runs the new_row_action() function on each one
    '''
    pass

def new_row_action(row_values, row_index):
    '''
    Peforms the standard action for a new row being added to a sheet.
    The standard action is to make a new form, then link the new form to a new spreadsheet, and finally save both these values for future use.
    Lastly, update the completed/uncompleted field in the spreadsheet row index to TRUE
    '''
    pass


if __name__ == "__main__":
    values = read_new_rows(CREATION_FORM_ID)
    print(values)