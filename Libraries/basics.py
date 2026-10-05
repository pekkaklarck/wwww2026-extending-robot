from datetime import datetime, timedelta

from robot.api import logger


def simple_keyword():
    print("Hello!")


def one_argument(name):
    print(f"Hello, {name}!")


def default_values(name, greeting="Hello"):
    print(f"{greeting}, {name}!")


def varargs(*args):
    print("-".join(args))


def argument_conversion(start: datetime, duration: timedelta):
    print(start.year)
    print(duration.total_seconds())


def should_be_positive(number: int | float):
    if number <= 0:
        raise AssertionError(f"{number} is not positive")


def log_using_print():
    print("Hi!")
    print("Second line of the first message.")
    print("*INFO* Hi with explicit INFO level!")
    print("*DEBUG* Hello, DEBUG!")


def log_using_api():
    logger.info("Hello using INFO")
    logger.debug("Hi using <b>DEBUG</b>", html=True)


def return_something():
    return "something"
