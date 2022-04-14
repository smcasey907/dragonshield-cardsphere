import time
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


api_url = "multiversebridge.com/api/v1/cards/search?"
retry_strategy = Retry(
    total=5,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["HEAD", "GET", "OPTIONS"],
    backoff_factor=2
)
adapter = HTTPAdapter(max_retries=retry_strategy)
http = requests.Session()
http.mount("https://", adapter)
sleepTimer = .5


def getCardData (query):
    time.sleep(sleepTimer)
    response = http.get(api_url, params=query)
    return response.json()
