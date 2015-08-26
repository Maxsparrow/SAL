import logging
import logging.config
import yaml
import os


def get_logger(logname):
    return logging.getLogger(logname)


def set_logger(logname, config_file='logging.yaml'):
    """Setup logging configuration
    """

    # Find current directory name
    current_dir_path = os.path.dirname(os.path.realpath(__file__))
    current_dir_name = os.path.split(current_dir_path)[1]

    logs_dir = os.path.abspath(os.path.join(current_dir_path, '..', 'logs'))
    # Create logs directory if it doesn't exist
    if not os.path.exists(logs_dir):
        print("Log dir does not exist, creating dir %s" % logs_dir)
        os.mkdir(logs_dir)

    # Set full path to output log file
    full_log_path = os.path.join(logs_dir, current_dir_name + '.log')

    # Open config file and read into logging config
    if os.path.exists(config_file):
        with open(config_file, 'rt') as f:
            config = yaml.load(f.read())
        config['handlers']['file_handler']['filename'] = full_log_path
        logging.config.dictConfig(config)
