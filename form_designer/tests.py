# TODO: Write some test that are actually beneficial
from django.test import TestCase

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.failUnlessEqual(1 + 1, 2)

class FormDefinitionTestCase(TestCase):
    pass

class FormDefinitionFieldTestCase(TestCase):
    pass