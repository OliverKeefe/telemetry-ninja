from pathlib import Path


class Telemetry:
    def __init__(self, ir=None, ir_status=None, ini_labels=None, logger=None):
        self.ir = ir
        self.ir_status = ir_status
        self.ini_labels = ini_labels
        self.logger = logger

    @staticmethod
    def get_ini_path() -> str:
        ini_file = Path("..", "config", "telemetry.ini")
        ini_file_path = str(ini_file.expanduser().resolve())
        return ini_file_path

    @staticmethod
    def telemetry_labels_parse(ini_labels: str, logger: object):
        parsed_labels = {}
        with open(ini_labels, "r") as ini_file:
            logger.debug(f"Parsing {ini_labels} to Python3 dict.")
            for line in ini_file:
                try:
                    line = line.split("#")[0].strip()
                    if "=" in line:
                        key, value = line.split("=", 1)
                        parsed_labels[key.strip()] = value.strip()
                except Exception as e:
                    logger.error(f"Error parsing {ini_labels} to Python3 dict: {e}")
        return parsed_labels

    @staticmethod
    def telemetry_get(ir: object, parsed_labels: dict, logger: object):
        telemetry_data = {}
        try:
            for key in parsed_labels.keys():
                telemetry_data[key] = ir[key]
            return telemetry_data
        except Exception as e:
            logger.error(f"Error getting telemetry data from iRacing: {e}")
            return {}
