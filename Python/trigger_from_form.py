#=========================================================------
#***PURPOSE***
#-------------
# Call the API and, conditionally, trigger an action for every form we have stored in the system
#
#
#
#***API data required***
#-----------------------
# Save the OAuth credentials, client secret, and any other information necessary when calling the API
#   -Do some research or messing around with chatGPT to discover which values are required
#   -Remember that we have an admin account to use, giving more privilege to API calls
#
#
#***Other data required***
#--------------------------
# Save the link to the master sheet
# Save the list of currently active form links in a .json file titled "program_data.json"
# "program_data.json" Dictionary Structure
#   {
#   "active_program_forms": [list of program titles],
#   "program_details": {"program_title" : {"title":"value", 'description':'value', 'etc':'value'}}
#   }
#
#***Functions required***
#-------------------------
# access_active_program_data():
#   read and return the file "program_data.json"
#
# check_form_trigger(form_link):
#   checks the Google Forms API for whether the given form (from link) has any new rows
#   returns the data from the api call, or a false flag
#
# add_data_to_google_sheets(data, sheet_link):
#   data is an object containing the name of the program the data came from and the response details from the form submission
#   calls the Google Sheets API to add the given details to the given spreadsheet as a new row (or multiple rows), including the name of the program the data came from
#
# check_all_forms():
#   retrieves the list of active program forms via access_active_program_data()
#   loops through every active program and
#   -gets its feedback form url
#   -runs function check_form_trigger(form_url)
#   -if the api call finds some new data, calls add_data_to_google_sheet(data, master_sheet_url)
#
#***OUTSIDE THE SCOPE OF THIS SCRIPT***
#---------------------------------------
#   > adding or removing keys or values from "program_data.json"
#   > calling the check_all_forms() function on a schedule (done outide by a different scheduler script)
#
#=========================================================------

import requests

def access_active_program_data():
    pass

def check_form_trigger(form_link):
    pass

def add_data_to_google_sheets(data, sheet_link):
    pass

def check_all_forms():
    pass
