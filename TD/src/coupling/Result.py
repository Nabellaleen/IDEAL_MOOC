class Result:
    """A result of an experience."""
    def __init__(self, label):
        self._label = label

    def get_label(self):
        return self._label
