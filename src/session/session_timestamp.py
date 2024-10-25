import datetime


class SessionTimeStamp:
    def __init__(self):
        pass

    def generate_timestamp() -> str:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
