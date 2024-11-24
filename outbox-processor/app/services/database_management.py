from db import database as db
import logging
import datetime

logging.basicConfig(level=logging.DEBUG)

last_timestamp = str()
next_timestamp = str()
timestamps_arr = list()


def init_db():
    global last_timestamp
    global next_timestamp
    last_timestamp = datetime.datetime.now()
    next_timestamp = last_timestamp + datetime.timedelta(hours=1.1)
    pt_name = f"orders_{int(last_timestamp.timestamp())}"
    db.init_db(pt_name, last_timestamp, next_timestamp)
    db.create_outbox()
    timestamps_arr.append(last_timestamp)


def create_partition():
    global last_timestamp
    global next_timestamp
    last_timestamp = next_timestamp
    next_timestamp = last_timestamp + datetime.timedelta(hours=1)
    pt_name = f"orders_{int(last_timestamp.timestamp())}"
    db.create_partition(pt_name, last_timestamp, next_timestamp)
    timestamps_arr.append(last_timestamp)
    if len(timestamps_arr) == 4:
        index_name = f"index_orders_{timestamps_arr[0]}"
        db.drop_index(index_name)
        timestamps_arr.remove(timestamps_arr[0])


    
    


