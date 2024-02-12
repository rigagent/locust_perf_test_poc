from locust import task
from src.locustfiles.test_areas.base import TestBase


class TestAPI(TestBase):

    def __init__(self, parent):
        super().__init__(parent)
        self.headers = {}

    @task
    def get_main_endpoint(self):
        with self.client.get('/', name='/', headers=self.headers, catch_response=True) as response:
            self.validate_response(response)

    @task
    def get_contacts_endpoint(self):
        with self.client.get('/contacts.php', name='/contacts.php', headers=self.headers,
                             catch_response=True) as response:
            self.validate_response(response)

    @task
    def get_news_endpoint(self):
        with self.client.get('/news.php', name='/news.php', headers=self.headers, catch_response=True) as response:
            self.validate_response(response)

    @task
    def get_pi_endpoint(self):
        with self.client.get('/pi.php?decimals=3', name='/pi.php?decimals=3', headers=self.headers,
                             catch_response=True) as response:
            self.validate_response(response)

    @task
    def get_browser_endpoint(self):
        with self.client.get('/browser.php', name='/browser.php', headers=self.headers,
                             catch_response=True) as response:
            self.validate_response(response)
