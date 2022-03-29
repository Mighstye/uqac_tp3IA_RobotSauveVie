""" Implementation of Borg Idiom to modify the Environment from env_objects class without having to pass the envi
# to it. """


class Borg:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state
