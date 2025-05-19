def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to use")
    parser.addoption("--url", action="store", default="http://localhost", help="Base URL")

import pytest

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture
def url(request):
    return request.config.getoption("--url")
