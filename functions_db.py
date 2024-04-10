from tinydb import TinyDB, Query
from automation import data
import os

# -----
# from original file
from tinydb import TinyDB, Query
from functions_ui import *


async def check_database_for_data(expected_list_name: str, expected_reminder_name: str):
    # Get the parent directory path
    parent_dir = os.path.dirname(os.path.dirname(__file__))

    # Construct the full path to db.json
    db_path = os.path.join(parent_dir, 'reminder_db.json')
    db = TinyDB(db_path)

    reminder_list_found = False
    ReminderList = Query().reminder_lists
    # print(ReminderList.dict)
    reminder_list_name = str(ReminderList.name == expected_list_name)
    # print(f'\n{reminder_list_name}')
    result1 = reminder_list_name.find(expected_list_name)
    # print(result1)
    if result1 >= 0:
        reminder_list_found = True

    reminder_item_found = False
    ReminderItemName = Query().reminder_item_name
    reminder_item_name = str(ReminderItemName.description == expected_reminder_name)
    # print(f'\n{reminder_item_name}')
    result2 = reminder_item_name.find(expected_reminder_name)
    # print(result2)
    if result2 >= 0:
        reminder_item_found = True

    return reminder_list_found and reminder_item_found

