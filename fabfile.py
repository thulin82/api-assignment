from invoke import task
import requests
from retry import retry

@task
def petstore_accessible(c, url=None):
    url = "http://localhost:8080" if url is None else url
    return verify_access(url)

@retry(tries=10, delay=2)
def verify_access(url):
    response = requests.get(url)
    if (response.status_code != 200):
        raise Exception(f"Not accessible url: '{url}''")
    print(f"Correctly verified: '{url}'\n")
    return True