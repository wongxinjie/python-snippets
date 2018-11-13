import traceback

import requests

url = "http://httpbin.org/ip"


def get_computer_ip(url):
    resp = requests.get(url)
    ip = resp.json()
    traceback.print_stack()
    return ip


if __name__ == "__main__":
    print(get_computer_ip(url))
