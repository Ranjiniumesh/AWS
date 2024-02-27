import logging

logging.basicConfig(level=logging.INFO, format='| %(levelname)-15s | %(asctime)s | %(name)s | %(lineno)-4s ::  %(message)s')

logger = logging.getLogger("test")

print("testinglogger")

logger.info("testinglogger")
