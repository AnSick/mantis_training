import pytest
from fixture.application import Application
import json
import os.path
import importlib

fixture = None
target = None

def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


@pytest.fixture
def app(request):
    global fixture
    web_config = load_config(request.config.getoption("--target"))['web']
    webadmin_config = load_config(request.config.getoption("--target"))['webadmin']
    browser = request.config.getoption("--browser")
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, baseUrl=web_config['baseUrl'])
    fixture.session.ensure_login(username=webadmin_config['username'], password=webadmin_config['password'])
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action = "store", default = "firefox")
    parser.addoption("--target", action = "store", default = "target.json")


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata
