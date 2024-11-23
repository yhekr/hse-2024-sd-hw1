import schedule
import time
from services.cancellation_processor import outbox_fetch
from db import database as db

schedule.every(3).seconds.do(outbox_fetch) # настроить время

def main():
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()