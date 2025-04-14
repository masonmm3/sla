function doGet(e) {
  var functionName = e.parameter.function; // Get the function name from the URL
  var f_id = e.parameter.f_id;             // Get the f_id parameter
  var s_id = e.parameter.s_id;             // Get the s_id parameter
  var title = e.parameter.title;          //Get the title parameter
  
  // Call the function dynamically based on the parameter
  if (functionName === "linkFormToSheet") {
    return linkFormToSheet(f_id, s_id);
  } else if (functionName === "linkFormToNewSheet") {
    return linkFormToNewSheet(f_id, title);
  } else if (functionName === "createNewForm"){
    return createNewForm();
  } else if (functionName === "duplicateForm") {
    return duplicateForm(f_id, title);
  } else {
    return HtmlService.createHtmlOutput("Function not found. Instead: "+ String(e.parameter));
  }
}

function linkFormToSheet(f_id, s_id) {
  var form = FormApp.openById(f_id);
  
  // Link the form to the Google Sheet
  form.setDestination(FormApp.DestinationType.SPREADSHEET, s_id);
  
  Logger.log('Form ' + f_id + ' is now linked to: ' + s_id);
}

function linkFormToNewSheet(f_id, title) {
  var form = FormApp.openById(f_id);
  
  var newSheet = SpreadsheetApp.create(title);  // Create a new sheet
  var s_id = newSheet.getId();
  form.setDestination(FormApp.DestinationType.SPREADSHEET, s_id);
  
  Logger.log('Form ' + f_id + ' is now linked to new sheet: ' + s_id);

  // Return the ID as JSON
  return ContentService.createTextOutput(JSON.stringify({ sheetId: s_id }))
    .setMimeType(ContentService.MimeType.JSON);
}

function createNewForm() {
  //pass
}

function duplicateForm(f_id, title) {
  const originalFormFile = DriveApp.getFileById(f_id);
  const copiedFile = originalFormFile.makeCopy(title);
  const copiedForm = FormApp.openById(copiedFile.getId());

  Logger.log(`New form created: ${copiedForm.getEditUrl()}`);

  // Return the ID as JSON
  return ContentService.createTextOutput(JSON.stringify({ formId: copiedForm.getId() }))
    .setMimeType(ContentService.MimeType.JSON);
}

function test() {
  //Logger.log("test ran")
  //duplicateForm('19DiZMuiejDLgYUKLmP5sGO66BR7rhoiZrQ-_KjKLISI', 'new_1')
}
