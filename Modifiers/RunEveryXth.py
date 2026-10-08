"""Pre-run modifier to select only every Xth test for execution.

Usage:
    robot --prerunmodifier RunEveryXth.py[:x][:start] path/to/tests.robot
"""

from robot.api import SuiteVisitor, TestSuite


class RunEveryXth(SuiteVisitor):

    def __init__(self, x: int = 2, start: int = 0):
        self.x = x
        self.start = start

    def start_suite(self, suite: TestSuite):
        suite.tests = suite.tests[self.start::self.x]
