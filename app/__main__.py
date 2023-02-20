
from .app import *

if __name__ == '__main__':
    def run_app():
        scheduler.add_job(id='Insert Venmo Transactions', func=add_transactions,
                          trigger="interval", seconds=20)  # for testing, change "days" to "seconds"
        scheduler.start()
        app.run(host="localhost", port=9090, debug=True, use_reloader=False)

run_app()
