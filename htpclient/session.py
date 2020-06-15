import requests
from urllib3.exceptions import InsecureRequestWarning

# We can't enable cert verification in this demo setting.
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


class Session:
    __instance = None

    def __new__(cls, s=None):
        if Session.__instance is None:
            Session.__instance = object.__new__(cls)
            Session.__instance.s = s
        return Session.__instance
