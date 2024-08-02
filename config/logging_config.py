import logging
import logging.config

def setup_logging(log_file='app.log', log_level=logging.ERROR):
    logging_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            },
            'detailed': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s\n%(exc_info)s'
            },
        },
        'handlers': {
            'console': {
                'level': log_level,  # Set the console logging level based on the log_level parameter
                'class': 'logging.StreamHandler',
                'formatter': 'standard',
            },
            'file': {
                'level': 'DEBUG',  # Log everything to the file
                'class': 'logging.FileHandler',
                'filename': log_file,
                'formatter': 'detailed',  # Use the detailed formatter for file handler
            },
        },
        'root': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',  # Set the root logger level
        },
    }

    logging.config.dictConfig(logging_config)