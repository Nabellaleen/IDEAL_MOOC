from coupling.interaction import Interaction


class Interaction010(Interaction):
    """docstring for Interaction010"""
    def __init__(self, label):
        self._label = label

    def get_label(self):
        """ @return The interaction's label"""
        return self._label

    def get_experience(self):
        """ @return The interaction's experience"""
        return self._experience

    def get_result(self):
        """ @return The interaction's result"""
        return self._result

    def set_experience(self, experience):
        """ @param experience: The interaction's experience."""
        self._experience = experience

    def set_result(self, result):
        """ @param result: The interaction's result."""
        self._result = result
