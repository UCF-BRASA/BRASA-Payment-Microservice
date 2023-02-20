
import os
from dotenv import load_dotenv

# loading the .env file
load_dotenv('.env')


class Keys():
    DB_URI = os.getenv('DB_URI')
    ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
    MY_USER_ID = os.getenv('ID')
    DB_NAME = 'brasa-app'
    VENMO_COLECT = 'brasa-venmo-transactions'
    CAPP_COLECT = 'brasa-cashapp-transactions'
    SHEETS_CREDs = 'sheets_creds.json'
    SHEETS_FILE_NAME = "VenmoScriptTest"
    MAX_SHEETS_COLS = 5
    TRANSACTIONS_SHEET = "Venmo Transactions"


google_api_scope = [
    "https://spreadsheets.google.com/feeds",
    'https://www.googleapis.com/auth/spreadsheets',
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]
