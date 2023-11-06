import sys
import irsdk
import time
import os
from pathlib import Path
from logconfig import LogConfiguration
from telemetry import Telemetry
from database import Database


def main():
    # Create Logger object, specify log file name, path and enable logging.
    logger, file_handler, formatter = LogConfiguration.enable(
        "TelemetryNinja",
        LogConfiguration.get_log_path(),
        "%(asctime)s - %(levelname)s - %(message)s",
    )
    logger.info("Telemetry Ninja was started.")

    # Connect to iRacing Simulator SDK using pyirsdk module.
    ir = irsdk.IRSDK()
    try:
        ir.startup()
        logger.debug("Successfully connected to iRacing Simulator.")
    except Exception as e:
        logger.error(f"Error connecting to iRacing Simulator: {e}")
        sys.exit(1)

    telemetry_labels = Telemetry.get_ini_path()
    parsed_labels = Telemetry.telemetry_labels_parse(telemetry_labels, logger)
    database_attributes = Database.database_attributes_create(logger)
    telemetry_data = Telemetry.telemetry_get(ir, parsed_labels, logger)

    # If the car is on the track, Telemetry Ninja will start capturing telemetry data, otherwise it will wait for 2 seconds and try again.
    while True:
        if ir["IsOnTrack"]:
            logger.info("Car is on track.")
            if not Path("telemetry_ninja.db").exists():
                # TODO: Look at this, change names of this method, this is for creating Database, not just table.
                Database.table_create(
                    database_name="telemetry_ninja.db",
                    database_connection=Database.database_connect(
                        database_name="telemetry_ninja.db",
                        database_manager="sqlite3",
                        logger=logger,
                    ),
                    telemetry_data=telemetry_data,
                    logger=logger,
                )

            # Establish database connection and create table
            database_connection = Database.database_connect(
                database_name="telemetry_ninja.db",
                database_manager="sqlite3",
                logger=logger,
            )

            telemetry_data = Telemetry.telemetry_get(ir, parsed_labels, logger)
            Database.table_insert(
                "telemetry",
                database_connection,
                telemetry_data,
                logger,
            )
            # print(f"Telemetry: {telemetry}")
            print(f"Telemetry: {telemetry_data}")
            sys.exit(1)
        else:
            logger.info("Car is not on track.")
            time.sleep(2)


if __name__ == "__main__":
    main()
