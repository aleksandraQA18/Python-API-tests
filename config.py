from dotenv import load_dotenv
import os
import logging

import requests

load_dotenv()

API_URL = os.getenv("API_URL")
SESSION = requests.Session()
LOG = logging.getLogger()
