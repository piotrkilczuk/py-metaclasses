from mock import sentinel


__all__ = (
    'FieldsMeta', 'SimpleForm', 'NoOpMeta', 'SimplestPossibleClass', 'WithNoOpMetaClass',
)


class FieldsMeta(type):

    def __new__(cls, name, bases, dct):
        new_dct = {k: v for k, v in dct.items() if (k.startswith('__') and k.endswith('__'))}
        new_dct['fields'] = {k: v for k, v in dct.items() if not (k.startswith('__') and k.endswith('__'))}
        return super(FieldsMeta, cls).__new__(cls, name, bases, new_dct)


class SimpleForm(metaclass=FieldsMeta):

    field1 = sentinel.field1
    field2 = sentinel.field2


class NoOpMeta(type):
    pass


class SimplestPossibleClass(object):
    pass


class WithNoOpMetaClass(object, metaclass=NoOpMeta):
    pass