#!/usr/bin/env python

"""Utility to mark test that take too long time failed.

Can be used either as a separate script or as a pre-Rebot modifier as part of
execution or when using Rebot.

Usage as a modifier:
    robot --prerebotmodifier FailSlow.py:threshold path/to/tests.robot
    rebot --prerebotmodifier FailSlow.py:threshold path/to/output.xml

Usage as a script:
    python FailSlow.py threshold output_file

Notice that when used as part of execution, statuses reported on the console
and in the output file are not affected. Changes are seen only in the generated
log and report files.
"""

import sys
from datetime import timedelta

from robot.api import SuiteVisitor, ExecutionResult
from robot.result import TestCase


class FailSlow(SuiteVisitor):

    def __init__(self, threshold: timedelta):
        self.threshold = threshold

    def start_test(self, test: TestCase):
        if test.passed and test.elapsed_time > self.threshold:
            test.status = "FAIL"
            test.message = f'Execution time was over {self.threshold}.'


if __name__ == "__main__":
    try:
        threshold, path = sys.argv[1:]
    except ValueError:
        sys.exit("Usage: FailSlow.py <threshold> <path>")
    result = ExecutionResult(path)
    visitor = FailSlow(timedelta(seconds=float(threshold)))
    result.suite.visit(visitor)
    result.save()
