#! /usr/bin/env python

#
# The run_tests.py file aims at running all tests that are supposed to be executed within the application
#   at first we import the base library paths and then we run the tests
#

import sys
import unittest

sys.path.append(".")

from tests.handlers.task_test import TaskHandlerTest

if __name__ == "__main__":
  unittest.main()
