import uuid


class SessionUUID:
    def __init__(self):
        pass

    def generate_uuid() -> str:
        return uuid.uuid4()
