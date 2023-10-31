import sqlite3
import configparser
import json
import time
import uuid
import logging
from telemetry import Telemetry


class Database:
    def __init__(
        self,
        database_attributes: dict,
        database_name: str,
        database_manager: str,
        database_connection: object,
        debug: bool,
    ) -> None:
        self.database_attributes = database_attributes
        self.database_name = database_name
        self.database_manager = database_manager
        self.database_connection = database_connection
        self.debug = debug

    def database_attributes_create(debug: bool) -> dict:
        config = configparser.ConfigParser()
        config.optionxform = str  # Retains pascal case formatting on keys, this is imperative for interacting with the iRacing SDK.
        config.read(Telemetry.get_ini_path())

        if debug == True:
            logging.debug(f"Creating database attributes.")

        logging.info("Sections found:", config.sections())
        database_attributes = {}

        for section in config.sections():
            for key, value in config.items(section):
                database_attributes[key.strip()] = value.strip()
        return database_attributes

    def database_connect(
        database_name: str, database_manager: str, debug: bool
    ) -> object:
        if database_manager.lower() == "sqlite3":
            return sqlite3.connect(database_name)

    def unique_entry_identifier_create() -> str:
        t = time.localtime()
        time_now = time.strftime("%H:%M:%S", t)
        return str(f"{time_now} - {uuid.uuid4()}")

    # TODO: Potential issue with this method, more debugging needed...
    def table_create(
        database_name: str,
        database_attributes: dict,
        database_connection: object,
        debug: bool,
    ) -> None:
        if debug == True:
            logging.debug(f"Creating database table.")

        columns = []
        columns.append("UniqueEntryIdentifier TEXT PRIMARY KEY")

        try:
            for attr, value in database_attributes.items():
                if isinstance(value, int):
                    columns.append(f"{attr} INTEGER")
                elif isinstance(value, float):
                    columns.append(f"{attr} FLOAT")
                else:
                    columns.append(f"{attr} TEXT")
        except Exception as e:
            logging.error(f"Error ascertaining column datatypes: {e}")

            columns_to_string = ", ".join(columns)
            cursor = database_connection.cursor()

        try:
            with database_connection:
                cursor.execute(
                    f"CREATE TABLE IF NOT EXISTS telemetry ({columns_to_string})"
                )

            # database_connection.commit()
        except Exception as e:
            logging.error(f"Error creating database table: {e}")

    # TODO: Fix this method. It's not inputting data into the table for some reason.
    @staticmethod
    def table_insert(
        table_name: str,
        database_connection: object,
        database_attributes: dict,
        debug: bool,
    ) -> None:
        serialized_database_attributes = [
            json.dumps(val) if isinstance(val, list) else val
            for val in database_attributes.values()
        ]
        columns = "UniqueEntryIdentifier, " + ", ".join(database_attributes.keys())
        placeholders = "?, " + ", ".join(["?"] * len(database_attributes))
        new_entry_uuid = Database.unique_entry_identifier_create()

        with database_connection:
            cursor = database_connection.cursor()
            cursor.execute(
                f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})",
                (new_entry_uuid, *serialized_database_attributes),
            )
