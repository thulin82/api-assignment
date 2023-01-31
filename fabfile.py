import requests
from retry import retry
from fabric.api import env, task, run, execute, put, get, local, warn_only

@task
@retry(tries=10, delay=2)
def verifyUrl(url):
    print("Verifying!")
    response = requests.get(url)
    if (response.status_code != 200):
        raise Exception(f"Not accessible url: '{url}'")
    print(f"Correctly verified: '{url}'\n")
    return True