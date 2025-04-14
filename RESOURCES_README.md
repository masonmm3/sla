# Explanation and links to important resources

* Program Creation Form:
* SLA program coordinators can enter basic information about the program here
* Our scripts will detect new data entering a spreadsheet from this form
* When new data is added, we will create a new feedback form and link a spreadsheet to it
* Finally, we will send an email containing the links to the new form and sheet
* Form: https://docs.google.com/forms/d/11F39xxlEFb7kzXuEM06T3IfHaIzaUu1AKU_90Ctu77E/edit
* Connected Spreadsheet: https://docs.google.com/spreadsheets/d/1GCE8SIKYwvZ8YNni_V0cHsCPmJD9pfps2NY1AjdBOJg/edit?resourcekey=&gid=95072625#gid=95072625

* Google Apps Script:
* The Google Apps Script service has much more control over google services (sheets, forms, drive, etc.)
* This script can be called via API to perform the more complex actions.
    * Creating new forms and spreadsheets.
    * Linking a form to a spreadsheet.
    * Duplicating forms from previously created ones.
* Before any changes to the script will come to effect, you must make a new deployment version in the app script.
* After completing any changes, update the text file at SLA/Archive/app_script.gs in this repository to match the code.
* https://script.google.com/u/2/home/projects/1Eg52dawiUREWuE2Q6M7XcV3NEjZuX0JTir1DrWDA8AFChFt2CE3C-nZD/edit