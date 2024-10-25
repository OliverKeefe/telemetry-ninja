import sqlite3
import configparser
import json
import time
import uuid
from telemetry import Telemetry


class Database:
    def __init__(
        self,
        database_attributes: dict,
        database_name: str,
        database_manager: str,
        database_connection: object,
        logger: object,
    ) -> None:
        self.database_attributes = database_attributes
        self.database_name = database_name
        self.database_manager = database_manager
        self.database_connection = database_connection
        self.logger = logger

    def database_attributes_create(logger: object) -> dict:
        config = configparser.ConfigParser()
        config.optionxform = str  # Retains pascal case formatting on keys, this is imperative for interacting with the iRacing SDK.
        config.read(Telemetry.get_ini_path())
        logger.debug(f"Creating database attributes.")
        logger.info("Sections found:", config.sections())
        database_attributes = {}

        for section in config.sections():
            for key, value in config.items(section):
                database_attributes[key.strip()] = value.strip()
        return database_attributes

    def database_connect(
        database_name: str, database_manager: str, logger: object
    ) -> object:
        logger.info(f"Connecting to {database_manager} database.")
        if database_manager.lower() == "sqlite3":
            return sqlite3.connect(database_name)

    def unique_entry_identifier_create() -> str:
        t = time.localtime()
        time_now = time.strftime("%H:%M:%S", t)
        return str(f"{time_now}:{uuid.uuid4()}")

    # TODO: Potential issue with this method, more debugging needed...
    def table_create(
        database_name: str,
        database_connection: object,
        telemetry_data: dict,
        logger: object,
    ) -> None:
        logger.debug(f"Creating database table.")
        columns = []
        columns.append("UniqueEntryIdentifier TEXT PRIMARY KEY")

        # for attr, value in database_attributes.items():
        #    if isinstance(value, int):
        #        columns.append(f"{attr} INTEGER")
        #    elif isinstance(value, float):
        #        columns.append(f"{attr} FLOAT")
        #    else:
        #        columns.append(f"{attr} TEXT")
        for attr, value in telemetry_data.items():
            if value is None:
                value = "None"
            if isinstance(value, int):
                columns.append(f"{attr} INTEGER")
            elif isinstance(value, float):
                columns.append(f"{attr} FLOAT")
            else:
                columns.append(f"{attr} TEXT")

        columns_to_string = ", ".join(columns)
        cursor = database_connection.cursor()

        with database_connection:
            cursor.execute(
                f"CREATE TABLE IF NOT EXISTS telemetry ({columns_to_string})"
            )

            database_connection.commit()

    # TODO: Fix this method. It's not inputting data into the table for some reason.
    @staticmethod
    def table_insert(
        table_name: str,
        database_connection: object,
        telemetry_data: dict,
        logger: object,
    ) -> None:
        new_entry_uuid = Database.unique_entry_identifier_create()
        serialized_telemetry_data = [
            json.dumps(val) if isinstance(val, list) else val
            for val in telemetry_data.values()
        ]
        columns = "UniqueEntryIdentifier, " + ", ".join(telemetry_data.keys())
        placeholders = "?, " + ", ".join(["?"] * len(telemetry_data))

        database_connection = sqlite3.connect("telemetry_ninja.db")
        with database_connection:
            cursor = database_connection.cursor()
            cursor.execute(
                f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})",
                (new_entry_uuid, *serialized_telemetry_data),
            )
