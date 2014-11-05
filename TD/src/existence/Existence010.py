from existence import Existence


class Existence010(Existence):
    """ An Existence010 simulates a "stream of intelligence" made of a
        succession of Experiences and Results.
        The Existence010 is SELF-SATISFIED when the Result corresponds to the
        Result it expected, and FRUSTRATED otherwise.
        Additionally, the Existence0 is BORED when it has been SELF-SATISFIED
        for too long, which causes it to try another Experience.
        An Existence1 is still a single entity rather than being split into an
        explicit Agent and Environment.
    """

    def __init__(self):
        pass

    def step(self):
        return 'Test'
