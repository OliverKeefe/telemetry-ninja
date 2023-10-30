import sys
import irsdk
from log_configuration import LogConfiguration
from telemetry import Telemetry


def main():
    debug: bool = True
    logger, file_handler, formatter = LogConfiguration.enable('TelemetryNinja', 
                                                              LogConfiguration.get_log_path(), 
                                                              '%(asctime)s - %(levelname)s - %(message)s')
    logger.info('Telemetry Ninja was started.')
    if irsdk.IRSDK() and debug == True:
        try:
            ir = irsdk.IRSDK()
            ir.startup()
            logger.debug('Successfully connected to iRacing Simulator.')
        except Exception as e:
            logger.error(f'Error connecting to iRacing Simulator: {e}')
            sys.exit(1)
    
    telemetry_labels = Telemetry.get_ini_path()    
    parsed_labels = Telemetry.telemetry_labels_parse(telemetry_labels, debug)


    if ir['IsOnTrack']:
        ir_status = 'IsOnTrack'
        logger.debug('Car is on track is on track.')
    
    while ir['IsOnTrack']:
        telemetry = Telemetry.telemetry_get(ir, parsed_labels, debug)
        print(f"Telemetry: {telemetry}")
if __name__ == '__main__':
    main()