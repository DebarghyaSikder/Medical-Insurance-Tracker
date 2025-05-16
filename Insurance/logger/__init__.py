import logging
from datetime import datetime
import os


LOG_DIR="Insurance_log"  # folder name

CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

LOG_FILE_NAME = f"log_{CURRENT_TIME_STAMP}.log"  # log file name

os.makedirs(LOG_DIR, exist_ok=True)  # create the folder if it doesn't exist

LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE_NAME)  # full path of the log file

logging.basicConfig(filename=LOG_FILE_PATH,
                    filemode='w',
                    format='[%(asctime)s: %(name)s]: %(message)s',
                    # level=logging.INFO,
                    level=logging.DEBUG,   # tells that what info to collect in logger file
                    
)