#=========================================================------
#***PURPOSE***
#-------------
# Call the API to check for new rows in each google sheet connected to an SLA seminar.
# Add each new row to the master sheet and mark it with its origin program
#
# DATA REQUIRED
#--------------------------
# Save the link to the master sheet
# Save the list of currently active google sheet links in a .json file titled "program_data.json"
# "program_data.json" Dictionary Structure
#   {
#   "active_programs": [list of program titles],
#   "program_details": {"program_title" : {"title":"value", 'description':'value', 'etc':'value'}},
#   "sheet_links": {"program_title":"sheet_link"}
#   }
#
# FUNCTIONS
#-------------------------
# access_active_program_data():
#   read and return the file "program_data.json"
#
# check_sheets_trigger(sheet_link):
#   checks the Google Sheets API for whether the given google sheet has any new rows
#   returns the data from the api call, or a false flag
#
# add_data_to_master_sheet(data, master_sheet_link):
#   data is an object containing the name of the program the data came from and the response details from the new spreadsheet row
#   calls the Google Sheets API to add the given details to the master spreadsheet as a new row (or multiple rows), including the name of the program the data came from
#
# check_all_sheets():
#   retrieves the list of active program forms via access_active_program_data()
#   loops through every active program and
#   -gets its feedback form's connected sheet url
#   -runs function check_sheet_trigger(sheet_url)
#   -if the api call finds some new data, calls add_data_to_master_sheet(data, master_sheet_url)
#
#***OUTSIDE THE SCOPE OF THIS SCRIPT***
#---------------------------------------
#   > adding or removing keys or values from "program_data.json"
#   > calling the check_all_forms() function on a schedule (done outide by a different scheduler script)
#
#=========================================================------

import requests
import json


def access_active_program_data():
    '''
    Read and return the file "program_data.json"
    '''
    pass

def check_sheets_trigger(sheet_link):
    '''
    Checks the Google Sheets API for whether the given google sheet has any new rows
    returns the data from the api call, or a false flag
    '''
    pass

def add_data_to_master_sheet(data, master_sheet_link):
    ''' 
    Calls the Google Sheets API to add the given details to the master spreadsheet as a new row (or multiple rows), including the name of the program the data came from
    This function may require logic as to which parts of the row go to which columns, since programs may have additional unique feedback fields.
    '''
    pass

def check_all_sheets():
    '''
    retrieves the list of active program forms via access_active_program_data()
    loops through every active program and
    -gets its feedback form's connected sheet url
    -runs function check_sheet_trigger(sheet_url)
    -if the api call finds some new data, calls add_data_to_master_sheet(data, master_sheet_url)
    '''
    pass