from dotenv import load_dotenv
import os
load_dotenv()

LOGIN = os.getenv('E_LOGIN')
PASSWORD = os.getenv('E_PASSWORD')



#For jenkins runs
DOMAIN = 'http://website:8000'
BASE_URL = 'http://website:8000'



#For local runs
#DOMAIN = '127.0.0.1'
#BASE_URL = 'http://127.0.0.1:8000'

# FOR API
LOGIN_ENDPOINT = '/login'
GET_ALL_REMINDERS_ENDPOINT = '/api/reminders'
GET_ALL_LISTS = f'{BASE_URL}/api/reminders'
GET_LIST_REMINDER_BY_ID = f'{BASE_URL}/api/reminders/items'

RESP_OK = 200
# RESP_CREATED = 201
# RESP_BAD_REQ = 400
# RESP_UNAUTH = 401
# RESP_NOT_FORBIDEN = 404
# RESP_NOT_FOUND = 404
# RESP_VALIDATION_ERROR = 422
