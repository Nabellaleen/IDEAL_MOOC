class Experiment:
    """ An experiment that can be chosen by the agent. """

    def __init__(self, label):
        self._label = label

    def get_label(self):
        return self._label
