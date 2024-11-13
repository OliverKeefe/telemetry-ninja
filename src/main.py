import sys
import irsdk
import time
import os
import argparse
from pathlib import Path
from logger.logconfig import LogConfiguration
from telemetry import Telemetry
from database.controller.sqlite_controller import Database


def main(sim, db):
    if db == "sqlite3":
        sqlite: bool = True
    else:
        print("MySQL and PostgresSQL not supported yet.")
        sys.exit(1)

    # Create Logger object, specify log file name, path and enable logging.
    logger, file_handler, formatter = LogConfiguration.enable(
        "TelemetryNinja",
        LogConfiguration.get_log_path(),
        "%(asctime)s - %(levelname)s - %(message)s",
    )
    logger.info("Telemetry Ninja was started.")

    # Connect to iRacing Simulator SDK using pyirsdk module.
    if (sim == "iRacing"):
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
            if sqlite == True:
                if not Path("telemetry_ninja.db").exists():
                    # TODO: Look at this, change names of this method, this is for creating Database, not just table.
                    try:
                        Database.create(
                            database_name="telemetry_ninja.db",
                            database_connection=Database.database_connect(
                                database_name="telemetry_ninja.db",
                                database_manager="sqlite3",
                                logger=logger,
                            ),
                            telemetry_data=telemetry_data,
                            logger=logger,
                        )

                    except:
                        logger.error(
                            "Error, unable to create SQLite3 test database.")

                try:
                    # Establish database connection and create table
                    database_connection = Database.database_connect(
                        database_name="telemetry_ninja.db",
                        database_manager="sqlite3",
                        logger=logger,
                    )
                except:
                    logger.error(
                        "Error, unable to connect to the SQLite3 test database.")

                telemetry_data = Telemetry.telemetry_get(
                    ir, parsed_labels, logger)
                Database.table_insert(
                    "telemetry",
                    database_connection,
                    telemetry_data,
                    logger,
                )
                print(f"Telemetry: {telemetry_data}")
            else:
                print("Only sqlite3 is supported currently, aboirting...")
                sys.exit(1)

        else:
            logger.info("Car is not on track.")
            time.sleep(2)
            resume = input("Resume? Y/N Default: [N]").strip().lower()

            if resume != "y":
                logger.info("Exiting...")
                sys.exit(1)
            else:
                logger.info("Resuming...")


# def arguments()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Telemetry Ninja")

    parser.add_argument(
        "-s",
        type=str,
        required=True,
        choices=["iRacing", "AssettoCorsa", "rFactor2",
                 "Formula 1 23", "Formula 1 24"],
        help="Specify the simulation platform (e.g., iRacing, AssettoCorsa, rFactor2)"
    )

    parser.add_argument(
        "-db",
        type=str,
        required=True,
        choices=["sqlite3", "mysql"],
        help="Specify the database to use (e.g., sqlite3, mysql)"
    )

    args = parser.parse_args()

    main(args.s, args.db)
