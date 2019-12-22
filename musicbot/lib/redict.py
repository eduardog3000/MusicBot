import re

class redict:
    def __init__(self, dict):
        self.__dict__ = dict
        pass

    def __getitem__(self, item):
        for key in self.__dict__:
            if re.fullmatch(key, item, re.IGNORECASE):
                return self.__dict__[key]

    def __contains__(self, item):
        for key in self.__dict__:
            if re.fullmatch(key, item, re.IGNORECASE):
                return True
        return False
