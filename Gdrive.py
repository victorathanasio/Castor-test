import gspread
import pandas as pd
from oauth2client.service_account import  ServiceAccountCredentials

def to_gdrive():
    # define the scope
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

    # add credentials to the account
    creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)

    # authorize the clientsheet
    client = gspread.authorize(creds)

    # get the instance of the Spreadsheet


    # client.create('Castor_output_')

    sheet = client.open('Castor_output')

    # get the first sheet of the Spreadsheet
    sheet_instance = sheet.get_worksheet(0)

    df = pd.read_csv('sales_force.csv')


    sheet_instance.insert_rows(df.values.tolist())