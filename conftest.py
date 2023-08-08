pytest_plugins = [
    "driver.driver",
]


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

