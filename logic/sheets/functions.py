

import gspread
from oauth2client.service_account import ServiceAccountCredentials

from util.constants import Keys, google_api_scope

sheets_creds = ServiceAccountCredentials.from_json_keyfile_name(
    Keys.SHEETS_CREDs, google_api_scope)

# open the client to access our Google Sheets
client = gspread.authorize(sheets_creds)


def send_to_sheets(new_transactions_list):

    inbound_list, outbound_list = separate_from_to(new_transactions_list)

    add_transactions_to_sheets(inbound_list, 1, 5, True)
    add_transactions_to_sheets(outbound_list, 7, 11, False)


# add new transactions in batch to Google Sheets
def add_transactions_to_sheets(new_transactions_list, first_col, last_col, isInbound):
    """ 
    (last updated 8/13/22)

    The purpose of the "global_index" variable is of the following example:

        Each BRASA transaction (currently) has 5 fields:
        - Transaction ID
        - Date
        - From/To (user)
        - Notes
        - Amount

        Cell iteration happens through columns, so one trasaction (currently) occupies 5 columns

        We need to create and iterate the "cell_list" keeping in mind that we lose track of where we left off. (due to Pythonic loops)
        That's where "global_index" comes to play, to ensure we keep our pointer on the "cell_list"  

    """
    global_index = 0

    # open the "transaction" sheet
    sheet = client.open(Keys.SHEETS_FILE_NAME).worksheet(
        Keys.TRANSACTIONS_SHEET)

    # get the rows that will be used
    if isInbound:
        first_row = len(sheet.get_values('A:A')) + 1
    else:
        first_row = len(sheet.get_values('G:G')) + 1

    last_row = first_row + len(new_transactions_list) - 1

    # create a cell list from a range (first column never change, so first_col=1)
    cell_list = sheet.range(first_row, first_col, last_row, last_col)

    # iterate through all transactions that are being inserted
    for last_rec in new_transactions_list:

        # general info
        transaction_id = last_rec['payment']['id']
        amount = last_rec['payment']['amount']
        date = last_rec['date_created']
        notes = last_rec['note']

        # for each iteration of the outter loop, go through a row and get the values in each cell
        # only iterate MAX_COL number of times to make it will fill only the appropriate number of spots
        for each_cell_index in range(Keys.MAX_SHEETS_COLS):

            # get the current cell's index (doing this because of loss of cursor through outter loop iterations)
            curr_index = global_index + each_cell_index

            # get the Cell reference to edit its info
            curr_cel = cell_list[curr_index]

            # from
            if isInbound:
                match curr_cel.col:
                    case 1:
                        curr_cel.value = transaction_id
                    case 2:
                        curr_cel.value = date
                    case 3:
                        curr_cel.value = last_rec['payment']['actor']['first_name'] + \
                            " " + last_rec['payment']['actor']['last_name']
                    case 4:
                        curr_cel.value = notes
                    case 5:
                        curr_cel.value = amount

            else:
                match curr_cel.col:
                    case 7:
                        curr_cel.value = transaction_id
                    case 8:
                        curr_cel.value = date
                    case 9:
                        curr_cel.value = last_rec['payment']['target']['user']['first_name'] + \
                            " " + \
                            last_rec['payment']['target']['user']['last_name']
                    case 10:
                        curr_cel.value = notes
                    case 11:
                        curr_cel.value = amount

        # after iterating MAX times, we update it to += MAX
        global_index += Keys.MAX_SHEETS_COLS

    # make a batch call to sheets and updates all the cells
    sheet.update_cells(cell_list)


def separate_from_to(new_transactions_list):

    # separate the lists based on actor and target
    inbound_list = [last_rec for last_rec in new_transactions_list if last_rec['payment']
                    ['target']['user']['id'] == Keys.MY_USER_ID]
    outbound_list = [last_rec for last_rec in new_transactions_list if last_rec['payment']
                     ['actor']['id'] == Keys.MY_USER_ID]

    return inbound_list, outbound_list
