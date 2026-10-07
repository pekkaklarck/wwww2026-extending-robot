from datetime import date
from enum import Enum
from typing import Literal, Self

from robot.api.deco import keyword, library
from robot.api.exceptions import ContinuableFailure, FatalError, SkipExecution
from robot.api.types import Secret


class TurnDirection(Enum):
    """Turn direction."""
    UP = "UP"
    DOWN = "DOWN"
    LEFT = "LEFT"
    RIGHT = "RIGHT"


class EuroDate(date):

    @classmethod
    def convert(cls, argument: str) -> Self:
        try:
            dd, mm, yyyy = argument.split(".")
            return cls(int(yyyy), int(mm), int(dd))
        except ValueError:
            raise ValueError(f"Expected date in format 'dd.mm.yyyy', got '{argument}'.")


@library(scope="SUITE", converters={EuroDate: EuroDate.convert})
class Advanced:

    def __init__(self, state: str = "not set"):
        self.state = state

    @keyword
    def state_should_be(self, expected: str):
        if self.state != expected:
            raise AssertionError(
                f"Expected state to be '{expected}' but it was '{self.state}'."
            )

    @keyword
    def set_state(self, state: str):
        print(f"Changing state from '{self.state}' to '{state}'.")
        self.state = state

    @keyword(name="Hello!")
    def hello(self):
        print("Hi!")

    @keyword(name="🤖", tags=["example", "robot"])
    def robot(self):
        pass

    @keyword("This is ${kind} example")
    def this_is_xxx_example(self, kind):
        print(kind)

    @keyword
    def move(self, direction: Literal["UP", "DOWN", "LEFT", "RIGHT"]):
        print(f"Moving {direction}.")

    @keyword
    def turn(self, direction: TurnDirection):
        print(f"Turning {direction.name}.")

    @keyword
    def workshop(self, start: EuroDate):
        print(start.day, start.month, start.year)

    @keyword
    def login(self, username: str, password: Secret):
        print(username, password.value)

    @keyword
    def skip_test(self):
        raise SkipExecution("Skipping test for some good reason")

    @keyword
    def fail_softly(self, message: str):
        raise ContinuableFailure(message)

    @keyword
    def fail_very_hard(self):
        raise FatalError("Stopping the whole execution!")
