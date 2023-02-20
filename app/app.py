
# general imports
import json
from flask import Flask, jsonify
from flask_apscheduler import APScheduler


# project imports
from util.functions import parse_json
from util.constants import Keys
from logic.sheets.functions import send_to_sheets
from logic.venmo.functions import DELETE_ALL_VENMO_DB_INFO, auth_user, get_most_recent_transaction, insert_venmo_trasactions, load_client

# check the virtual environment
# check_venv()

app = Flask(__name__)
scheduler = APScheduler()

# I will change this later to file-like configs
# app.config['JSON_SORT_KEYS'] = False
app.config.from_object('util.config.DevConfig')


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


def add_transactions():

    # check if auth is valid
    if auth_user() == False:
        return jsonify(
            {
                'error': 'Bad Auth'
            })

    # PART 1: Get transactions from Venmo Account
    new_transaction_list = load_client().user.get_user_transactions(Keys.MY_USER_ID)

    # PART 2: Get JSON from transactions

    # list of transactions that will be appended as JSON
    final_transaction_list = []

    # gets all the transactions JSON for easier use later on
    for each_trasaction in new_transaction_list:
        for attributes, val in each_trasaction.__dict__.items():

            # append the json info to the list
            if attributes == "_json":
                final_transaction_list.append(val)

    # PART 3: Compare to DB

    # get the most recent record from DB
    try:
        last_record = get_most_recent_transaction(Keys.VENMO_COLECT)
    except StopIteration:
        print('Empty cursor')

    # list that will be inverted to be inserted into DB
    db_insertion_list = []

    for each_transaction in final_transaction_list:

        # once we find the end of the new transactions, stop loop
        if each_transaction['id'] == last_record['id']:
            break

        # else, append info to list
        db_insertion_list.append(each_transaction)

    # PART 4: Add new info to DB (now Google Sheets)

    # invert the list and add it to the DB and Google Sheets
    if len(db_insertion_list) != 0:
        db_insertion_list.reverse()
        insert_venmo_trasactions(db_insertion_list)
        send_to_sheets(db_insertion_list)
        print("INFO ADDED")

    else:
        print("NO INFO :)")

    # return the added records in the order they were inserted
    return json.dumps(
        {
            'venmo_inserted_values': parse_json(db_insertion_list)
        })


# DEBUG: REMOVE THIS LATER!!!!!
@app.route('/delete_all_db', methods=['POST', 'GET'])
def delete_all_db():

    DELETE_ALL_VENMO_DB_INFO()

    return "done"
