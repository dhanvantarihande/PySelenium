# Logging means - You can add logs to the Failure, Information, Error
# If We want to give some Warning to the Users

import logging
def test_print_logs():
    LOGGER =logging.getLogger(__name__)
    LOGGER.info("This is Information Logs")
    LOGGER.warning("This is Warning Logs")
    LOGGER.error("This is Error Logs")
    LOGGER.critical("This is Critical Logs")
