# conftest.py
import pytest

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser to run tests on")
    parser.addoption("--url", action="store", help="url for testing")

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture
def url(request):
    return request.config.getoption("--url")
