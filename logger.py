import logging
from config import LOG_FILE

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def log_event(action, path):
    with open("logs/file_activity.log", "a") as f:
        f.write(f"{action} | {path}\n")


def log_alert(msg):
    logging.warning("ALERT: " + msg)

from datetime import datetime

def log_event(event_type, path, details=""):
    with open("logs/file_activity.log", "a") as f:
        f.write(
            f"{datetime.now()} | {event_type} | {path} | {details}\n"
        )

