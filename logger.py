import logging
import sys
from logtail import LogtailHandler

token = 'FrH19SS8aswmGE5LXQeRoEa4'

# get logger
logger = logging.getLogger()

# create formatter
formatter = logging.Formatter(
    fmt="%(asctime)s - %(levelname)s - %(message)s"
)

# create handlers
stream_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler('app.log', mode="w", encoding=None, delay=False)
#file_handler = logging.StreamHandler('app.log')
#better_stack_handler = logging.StreamHandler(source_token=token)

# set formatters
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# add handlers to the logger
#logger.handlers = [stream_handler, file_handler, better_stack_handler]
logger.handlers = [stream_handler, file_handler]

# set log-level
logger.setLevel(logging.INFO)