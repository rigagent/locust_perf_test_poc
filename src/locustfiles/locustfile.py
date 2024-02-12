from gevent import monkey

try:
    monkey.patch_all()
except ImportError:
    pass

import sys
import urllib3
from locust import HttpUser, between, events
from locust_influx import expose_metrics
from src.locustfiles.test_areas.test_api import TestAPI
from src.utils.config_reader import EnvConfig
from src.utils.events import on_additional_arguments


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
events.init_command_line_parser.add_listener(on_additional_arguments)
expose_metrics(interval_ms=2000)


class TestUser(HttpUser):
    env = EnvConfig()
    wait_time = between(int(env.locust_wait_time_min), int(env.locust_wait_time_max))
    host = env.locust_host
    tasks = {getattr(sys.modules[__name__], item.split(':')[0]): int(item.split(':')[1])
             for item in env.locust_tasks.split(',')}

    # wait_time = between(1, 2)
    # host = 'https://test.k6.io'
    # tasks = {TestAPI: 1}
