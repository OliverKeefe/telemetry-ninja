from pathlib import Path
from log_configuration import LogConfiguration
import logging


class Telemetry:
    def __init__(
        self, ir=None, ir_status=None, ini_labels=None, logger=None, debug=None
    ):
        self.ir = ir
        self.ir_status = ir_status
        self.ini_labels = ini_labels
        self.logger = logger
        self.debug = debug

    @staticmethod
    def get_ini_path() -> str:
        ini_file = Path("..", "config", "telemetry.ini")
        ini_file_path = str(ini_file.expanduser().resolve())
        return ini_file_path

    @staticmethod
    def telemetry_labels_parse(ini_labels: str, debug: bool):
        parsed_labels = {}
        with open(ini_labels, "r") as ini_file:
            if debug == True:
                logging.debug(f"Parsing {ini_labels} to Python3 dict.")
            for line in ini_file:
                try:
                    line = line.split("#")[0].strip()
                    if "=" in line:
                        key, value = line.split("=", 1)
                        parsed_labels[key.strip()] = value.strip()
                except Exception as e:
                    logging.error(f"Error parsing {ini_labels} to Python3 dict: {e}")
        return parsed_labels

    @staticmethod
    def telemetry_get(ir, parsed_labels, debug: bool):
        try:
            if debug == True:
                logging.debug(f"Getting telemetry data from iRacing.")
            for key, value in parsed_labels.items():
                value_from_ir = ir[key]
                parsed_labels[key] = value_from_ir
            return parsed_labels

        except Exception as e:
            logging.error(f"Error getting telemetry data from iRacing: {e}")
