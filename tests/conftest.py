import pytest
from dotenv import load_dotenv



if not load_dotenv("test.env"):
    load_dotenv("tests/test.env")



@pytest.fixture(scope="session")
def httpserver_listen_address():
    return ("localhost", 8888)
