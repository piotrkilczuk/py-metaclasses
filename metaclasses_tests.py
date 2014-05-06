from unittest import TestCase

from metaclasses import *


class SimplestPossibleTestCase(TestCase):

    def test_object_class(self):
        """
        An object of SimplestPossibleClass will have a .__class__ attribute == SimplestPossibleClass
        """
        simplest_possible_object = SimplestPossibleClass()
        self.assertEqual(simplest_possible_object.__class__, SimplestPossibleClass)

    def test_metaclass(self):
        """
        The SimplestPossibleClass will have a .__class__ attribute too == type
        """
        self.assertEqual(SimplestPossibleClass.__class__, type)
