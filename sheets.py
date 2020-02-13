import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import os.path
from gspread_dataframe import get_as_dataframe, set_with_dataframe
import gspread_dataframe as gd

#Hook up our sheet
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
ROOT_DIR = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
GDRIVE_PATH = ROOT_DIR + '\GoogleDriveAPIs\\'
creds = ServiceAccountCredentials.from_json_keyfile_name(GDRIVE_PATH + "BoardGeeks.json", scope)
client = gspread.authorize(creds)
master_file = client.open("Development Master Sheet")
prod = master_file.worksheet("Product")
inventory = master_file.worksheet("Inventory")
price = master_file.worksheet("Pricing")
orders = master_file.worksheet("Orders")