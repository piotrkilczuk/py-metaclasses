from unittest import TestCase

from mock import MagicMock, sentinel

from metaclasses import *


class FieldsMetaTestCase(TestCase):

    def test_dct_altered(self):
        form = SimpleForm()
        self.assertEqual(form.fields, {
            'field1': sentinel.field1,
            'field2': sentinel.field2,
        })


class SimplestPossibleTestCase(TestCase):

    def test_object_class(self):
        """
        An object of SimplestPossibleClass will have a .__class__ attribute == SimplestPossibleClass
        """
        simplest_possible_object = SimplestPossibleClass()
        self.assertEqual(simplest_possible_object.__class__, SimplestPossibleClass)

    def test_class_class(self):
        """
        The SimplestPossibleClass will have a .__class__ attribute too == type
        """
        self.assertEqual(SimplestPossibleClass.__class__, type)

    def test_type_used_as_metaclass(self):
        """
        A class is constructed by Python by default using type constructor
        """
        runtime_class = type('SimplestPossibleClass', (object,), {})
        self.assertEqual(SimplestPossibleClass.__class__, runtime_class.__class__)
        self.assertEqual(SimplestPossibleClass.__mro__[1:], runtime_class.__mro__[1:])


class WithNoOpMetaClassTestCase(TestCase):

    def test_new_and_init_called_on_metaclass(self):
        """
        When declaring new class the standard way, __new__ and __init__ shall be called with respective values
        """
        runtime_meta = type('RuntimeMeta', (type,), {
            '__new__': MagicMock(side_effect=type.__new__),
            '__init__': MagicMock(return_value=None),
        })

        runtime_class = runtime_meta('RuntimeClass', (object,), {})
        runtime_meta.__new__.assert_called_with(runtime_meta, 'RuntimeClass', (object,), {})
        runtime_meta.__init__.assert_called_with('RuntimeClass', (object,), {})