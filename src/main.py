from log_configuration import LogConfiguration

def main():
    logger, file_handler, formatter = LogConfiguration.enable('TelemetryNinja', 
                                                              LogConfiguration.get_log_path(), 
                                                              '%(asctime)s - %(levelname)s - %(message)s')
    logger.debug('This is a debug message')
    

if __name__ == '__main__':
    main()