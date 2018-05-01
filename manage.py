#!/usr/bin/python

import unittest
import xmlrunner

def test():
    """Run the unit tests."""
    tests = unittest.TestLoader().discover('tests')
    xmlrunner.XMLTestRunner(output=os.environ.get('CIRCLE_TEST_REPORTS','test-reports')).run(tests)
