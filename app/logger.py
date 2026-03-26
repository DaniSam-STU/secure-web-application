import datetime


def log_event(message):
    with open("security.log", "a", encoding="utf-8") as f:
        f.write(f"{datetime.datetime.now()} - {message}\n")