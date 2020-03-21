# Assorted functions
import pickle
import os.path
from googleapiclient.discovery import build


def initialize_sheets():
    # Get Credentials
    token_path = os.path.join(os.path.dirname(
        os.path.relpath(__file__)), "token.pickle")
    with open(token_path, 'rb') as token:
        creds = pickle.load(token)
    service = build('sheets', 'v4', credentials=creds)
    sheets = service.spreadsheets()

    # Initialize
    return sheets
