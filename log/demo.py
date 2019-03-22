import logging
import logging.handlers as handlers


logger = logging.getLogger('demo')
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
log_handler = handlers.TimedRotatingFileHandler(
    'rotate.log', when='M', interval=1
)
log_handler.setLevel(logging.INFO)
log_handler.setFormatter(formatter)
logger.addHandler(log_handler)

logger.info("test")
