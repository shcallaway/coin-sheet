# oauth 2 for python: http://bit.ly/2x7qyEg
# example implementation: http://bit.ly/2vbwMH0

import os, re, warnings

from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage

file = 'credentials.json'

def init_flow():
  # these come from google developer console
  CLIENT_ID = os.environ['CLIENT_ID']
  CLIENT_SECRET = os.environ['CLIENT_SECRET']

  if not CLIENT_ID or not CLIENT_SECRET:
    print 'CLIENT_ID or CLIENT_SECRET not available.'
    return False

  REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'
  SCOPE = 'https://www.googleapis.com/auth/spreadsheets'

  return OAuth2WebServerFlow(client_id=CLIENT_ID,
                             client_secret=CLIENT_SECRET,
                             scope=SCOPE,
                             redirect_uri=REDIRECT_URI)

def get_credentials( ):
  # allows me to catch 'no such file' warning
  warnings.filterwarnings('error')

  try:
    print 'Getting access tokens from storage.'
    storage = Storage(file)
    credentials = storage.get()

  except Warning:
    print 'No such file or dir: ' + file
    credentials = None

  # get new auth code and token
  if not credentials or credentials.invalid:
    flow = init_flow()

    print 'Visit this URL in your web browser:'

    # make url blue
    white = '\033[0m'
    blue = '\033[34m'

    print blue + flow.step1_get_authorize_url() + white
    
    code = raw_input('Enter your new authorization code here: ')

    credentials = flow.step2_exchange(code=code)

    print 'Writing access tokens to local file: ' + file
    storage = Storage(file)
    storage.put(credentials)

  return credentials
