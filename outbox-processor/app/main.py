import schedule
import time
from services.cancellation_processor import outbox_fetch
from services.database_management import init_db, create_partition
from db import database as db

schedule.every(3).seconds.do(outbox_fetch)
schedule.every(60).minutes.do(create_partition)

def main():
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    init_db()
    main()