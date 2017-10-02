import httplib2

# google-api-python-client: http://bit.ly/2x79GgQ
from apiclient.discovery import build
from apiclient.errors import HttpError

spreadsheet_id = '1FTMawTE_5qBvueDiNrxzIHl2V6YmXE0rQvDl8XcFfNk'

def init_service(credentials):
  http = credentials.authorize(httplib2.Http())

  discovery_url = ('https://sheets.googleapis.com/$discovery/rest?'
                   'version=v4')

  # docs: http://bit.ly/2yipSk8
  return build('sheets', 
               'v4', 
               http=http, 
               discoveryServiceUrl=discovery_url, 
               cache_discovery=False)

def update(a1range, values, credentials):
  service = init_service(credentials)

  body = {
    'range': a1range,
    'values': values
  }

  # docs: http://bit.ly/2xQccvB
  request = service.spreadsheets().values().update(
    spreadsheetId=spreadsheet_id,
    range=a1range,
    body=body,
    valueInputOption='USER_ENTERED',
    includeValuesInResponse=True
  )

  try: 
    response = request.execute()
    print 'Successfully updated spreadsheet.'
    return response
  except HttpError, error:
    print __name__ + '.update failed due to HttpError: ' + str(error.resp.status)
    return False

def append(a1range, values, credentials):
  service = init_service(credentials)

  body = {
    'range': a1range,
    'values': values
  }

  # docs: http://bit.ly/2xQccvB
  request = service.spreadsheets().values().append(
    spreadsheetId=spreadsheet_id,
    range=a1range,
    body=body,
    valueInputOption='USER_ENTERED',
    includeValuesInResponse=True
  )

  try: 
    response = request.execute()
    print 'Successfully updated spreadsheet.'
    return response
  except HttpError, error:
    print __name__ + '.append failed due to HttpError: ' + str(error.resp.status)
    return False
