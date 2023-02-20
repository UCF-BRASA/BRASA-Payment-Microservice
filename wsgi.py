
from app import *

if __name__ == '__main__':
    scheduler.add_job(id='Insert Venmo Transactions', func=add_transactions,
                      trigger="interval", days=1)  # for testing, change "days" to "seconds"
    scheduler.start()
    app.run(host="localhost", port=9090, debug=True, use_reloader=False)
