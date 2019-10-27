#UnitTest:
#Test fixture: A test fixture represents the preparation needed to perform one or more tests, and any associate cleanup actions. 
#This may involve, for example, creating temporary or proxy databases, directories, or starting a server process.

#Test case: A test case is the individual unit of testing. It checks for a specific response to a particular set of inputs. 
#unittest provides a base class, TestCase, which may be used to create new test cases.

#Test suite: A test suite is a collection of test cases, test suites, or both. It is used to aggregate tests that should be executed together.

#Test runner: A test runner is a component which orchestrates the execution of tests and provides the outcome to the user. 
#The runner may use a graphical interface, a textual interface, or return a special value to indicate the results of executing the tests.
# The test runner accumulates all test results and produce a report.

import unittest

#A testcase is created by subclassing unittest.TestCase
class TestStringMethods(unittest.TestCase):
	# 3 individual test. Naming convention informs the runner about which methods represent tests.
    # setUp() 
	def test_upper(self):
		# assertEqual() to check for an expected result
		self.assertEqual('foo'.upper(), 'FOO')
	# tearDown()

	# setUp() 
	def test_isupper(self):
		# assertTrue() or assertFalse() to verify a condition
		self.assertTrue('FOO'.isupper())
		self.assertFalse('Foo'.isupper())
	# tearDown()

	# setUp() 
	def test_split(self):
		s = 'hello world'
		self.assertEqual(s.split(), ['hello', 'world'])

		# assertRaises() to verify that a specific exception gets raised
        # check that s.split fails when the separator is not a string
		with self.assertRaises(TypeError):
			s.split(2)
	# tearDown()

#Provides command line interface CLI
if __name__ == '__main__':
    unittest.main()

# CLI Commands: for the unittest module

# unittest in the CLI can run modules, classes or even individual test methods:
# python -m unittest test_module1 test_module2
# python -m unittest test_module.TestClass
# python -m unittest test_module.TestClass.test_method

# Test modules can be specified by file path as well:
# python -m unittest tests/test_something.py
	# If you want to execute a test file that isn’t importable as a module you should execute the file directly instead.

# Testing with verbosity
# python -m unittest -v test_module

# When executed without arguments Test Discovery is started:
# python -m unittest

# For a list of all the command-line options:
# python -m unittest -h

# Command-line options:
#-b, --buffer
#-c, --catch
#-f, --failfast
#-k