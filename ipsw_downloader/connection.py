import requests
from requests import Session
from urllib3.util import Retry

DEFAULT_TIMEOUT = 1.5


class HTTPAdapterWithTimeout(requests.adapters.HTTPAdapter):
    def __init__(self, *args, **kwargs):
        self.timeout = kwargs.pop("timeout", DEFAULT_TIMEOUT)
        super(HTTPAdapterWithTimeout, self).__init__(*args, **kwargs)

    def send(self, request, **kwargs):
        timeout = kwargs.get("timeout")
        if timeout is None:
            kwargs["timeout"] = self.timeout
        return super(HTTPAdapterWithTimeout, self).send(request, **kwargs)


def session_with_retry(retries=None, backoff_factor=0):
    session = requests.Session()

    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        status_forcelist=[429, 500, 502, 504],
        backoff_factor=backoff_factor,
        method_whitelist=False,
    )
    adapter = HTTPAdapterWithTimeout(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session
