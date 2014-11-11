from coupling.interaction import Interaction010


class Interaction020(Interaction010):
    """ An Interaction020 is an Interaction010 with a valence. """

    def set_valence(self, valence):
        self._valence = valence

    def get_valence(self):
        return self._valence

    def __str__(self):
        return '{0},{1}'.format(self.get_label(), self.get_valence())
