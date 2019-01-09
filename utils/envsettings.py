import os


class EnvSettingMetaCls(type):
    def __new__(cls, name, bases, attrs):
        for k, v in attrs.items():
            if not k.startswith('__'):
                if isinstance(v, bool):
                    attrs[k] = cls.strpbool(os.getenv(k, v))
                    continue

                attrs[k] = type(v)(os.getenv(k, v))
        return type.__new__(cls, name, bases, attrs)

    @classmethod
    def strpbool(cls, value):
        if isinstance(value, bool):
            return value
        if value in ('true', u'true'):
            return True

        if value in ('false', u'false'):
            return False


class EnvSettingBase(object):
    __metaclass__ = EnvSettingMetaCls
    '''
        Here is default value.
            `FIELD = default`
        system will get envionment variables automatic like:
            `os.getenv('FIELD', default)`
        For detail behaviour, You can see the MetaClass.

        Warning !!! The default can not be `None`.
        If you fill a blank value, keep the same type. like:
            `DB_USER = ''`
    '''
