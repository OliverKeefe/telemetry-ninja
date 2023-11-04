import sys
import irsdk
import time
import os
from pathlib import Path
from logconfig import LogConfiguration
from telemetry import Telemetry
from database import Database


def main():
    debug: bool = True
    logger, file_handler, formatter = LogConfiguration.enable(
        "TelemetryNinja",
        LogConfiguration.get_log_path(),
        "%(asctime)s - %(levelname)s - %(message)s",
    )
    logger.info("Telemetry Ninja was started.")
    ir = irsdk.IRSDK()
    try:
        ir.startup()
        logger.debug("Successfully connected to iRacing Simulator.")
    except Exception as e:
        logger.error(f"Error connecting to iRacing Simulator: {e}")
        sys.exit(1)
    telemetry_labels = Telemetry.get_ini_path()
    parsed_labels = Telemetry.telemetry_labels_parse(telemetry_labels, debug)
    database_attributes = Database.database_attributes_create(debug)
    while True:
        if ir["IsOnTrack"]:
            logger.info("Car is on track.")
            if not Path("database/telemetry_ninja.db").exists():
                telemetry_data = Telemetry.telemetry_get(ir, parsed_labels, debug)

                # Establish database connection and create table
                database_connection = Database.database_connect(
                    database_name="telemetry_ninja.db",
                    database_manager="sqlite3",
                    debug=debug,
                )
                # TODO: Look at this, change names of this method, this is for creating Database, not just table.
                Database.table_create(
                    database_name="telemetry_ninja.db",
                    database_attributes=database_attributes,
                    database_connection=database_connection,
                    telemetry_data=telemetry_data,
                    debug=debug,
                )
            else:
                telemetry_data = Telemetry.telemetry_get(ir, parsed_labels, debug)
                Database.table_insert(
                    "telemetry",
                    database_connection,
                    database_attributes,
                    telemetry_data,
                    debug,
                )
            # print(f"Telemetry: {telemetry}")
            print(f"{telemetry_data}")
        else:
            logger.info("Car is not on track.")
            time.sleep(2)


if __name__ == "__main__":
    main()
