import json
import os
import os.path
from dotenv import load_dotenv


def read_config(config_file):
    with open(config_file, 'r') as f:
        json_data = json.load(f)
    return json_data


class EnvConfig:

    def __init__(self):
        load_dotenv(dotenv_path='..env')
        self.locust_file = os.getenv('LOCUST_LOCUSTFILE')
        self.locust_host = os.getenv('LOCUST_HOST')
        self.locust_tasks = os.getenv('LOCUST_TASKS')
        self.locust_wait_time_min = os.getenv('LOCUST_WAIT_TIME_MIN')
        self.locust_wait_time_max = os.getenv('LOCUST_WAIT_TIME_MAX')
        self.locust_html = os.getenv('LOCUST_HTML')
        self.locust_csv = os.getenv('LOCUST_CSV')
