import logging
from datetime import datetime
import os
import pandas as pd
import re

LOG_DIR = "logs"  # creating the directory as log

def get_current_time_stamp():
    '''Description : This function will return the current timestamp '''
    return datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

def get_log_file_name():
    '''Description : This function will create a log file to store the log '''
    return f"log_{get_current_time_stamp()}.log"

LOG_FILE_NAME = get_log_file_name()  # creating log file name

os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE_NAME)  # creating log file path

logging.basicConfig(filename=LOG_FILE_PATH,
                    filemode="w",
                    format='[%(asctime)s]%(name)s-%(levelname)s-%(message)s',
                    level=logging.INFO)  # this code will helps to create the log

def get_log_dataframe(file_path):
    '''This function will create the dataframe to store the log'''
    data = []
    log_pattern = re.compile(r'\[(.*?)\](.*?)\-(.*?)\-(.*)')

    with open(file_path) as log_file:
        for line in log_file.readlines():
            match = log_pattern.match(line)
            if match:
                timestamp, name, level, message = match.groups()
                data.append([timestamp, name, level, message])

    log_df = pd.DataFrame(data, columns=["Time stamp", "Logger Name", "Log Level", "Message"])
    log_df["log_message"] = log_df['Time stamp'].astype(str) + ": $" + log_df["Message"]

    return log_df[["log_message"]]

# Test the function with the created log file
logging.info("This is a test log message.")

log_df = get_log_dataframe(LOG_FILE_PATH)
print(log_df.head())
