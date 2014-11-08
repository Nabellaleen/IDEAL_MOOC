class Interaction:

    def get_label(self):
        """ @return The interaction's label"""
        raise NotImplementedError

    def get_experience(self):
        """ @return The interaction's experience"""
        raise NotImplementedError

    def get_result(self):
        """ @return The interaction's result"""
        raise NotImplementedError

    def set_experience(self, experience):
        """ @param experience: The interaction's experience."""
        raise NotImplementedError

    def set_result(self, result):
        """ @param result: The interaction's result."""
        raise NotImplementedError
