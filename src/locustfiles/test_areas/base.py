import logging
from locust import TaskSet
from src.utils.config_reader import *


class TestBase(TaskSet):

    def __init__(self, parent):
        super().__init__(parent)
        self.env_config = EnvConfig()
        self.success_status_codes = (200, 201, 204, 300, 301, 302, 304)

    def validate_response(self, response):
        if response.status_code in self.success_status_codes:
            response.success()
        else:
            response.failure(response.status_code)
            logging.critical(str(response.status_code))
