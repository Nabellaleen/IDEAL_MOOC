# Standard libraries
from enum import Enum

# Sibling packages
from coupling import Experiment
from coupling.interaction import Interaction010
from coupling import Result

# Current package
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

    LABEL_E1 = "e1"
    LABEL_E2 = "e2"
    LABEL_R1 = "r1"
    LABEL_R2 = "r2"

    Mood = Enum('Mood', 'SELF_SATISFIED FRUSTRATED BORED PAINED PLEASED')

    BOREDOME_LEVEL = 4

    def __init__(self):
        self._init_existence()

    def _init_existence(self):
        self._experiences = {}
        self._interactions = {}
        self._results = {}
        self._mood = self.Mood.SELF_SATISFIED
        self.set_self_satisfaction_counter(0)

        e1 = self._add_or_get_experience(self.LABEL_E1)
        self._add_or_get_experience(self.LABEL_E2)
        self.set_previous_experience(e1)

    def step(self):
        experience = self.get_previous_experience()
        if self.get_mood() is self.Mood.BORED:
            experience = self._get_other_experience(experience)
            self.set_self_satisfaction_counter(0)

        anticipated_result = self._predict(experience)

        result = self.return_result_010(experience)

        self._add_or_get_primitive_interaction(experience, result)

        if result is anticipated_result:
            self.set_mood(self.Mood.SELF_SATISFIED)
            self.inc_self_satisfaction_counter()
        else:
            self.set_mood(self.Mood.FRUSTRATED)
            self.set_self_satisfaction_counter(0)

        if self.get_self_satisfaction_counter() >= self.BOREDOME_LEVEL:
            self.set_mood(self.Mood.BORED)

        self.set_previous_experience(experience)

        return '{0}{1} {2}'.format(experience.get_label(),
                                   result.get_label(),
                                   self.get_mood())

    def _add_or_get_primitive_interaction(self, experience, result):
        """ Create an interaction as a tuple <experience, result>.
            @param experience: The experience.
            @param result: The result.
            @return The created interaction
        """
        interaction_label = '{0}{1}'.format(experience.get_label(),
                                            result.get_label())
        interaction = self._add_or_get_interaction(interaction_label)
        interaction.set_experience(experience)
        interaction.set_result(result)
        return interaction

    def _add_or_get_interaction(self, label):
        """ Records an interaction in memory.
            @param label: The label of this interaction.
            @return The interaction.
        """
        if label not in self._interactions:
            self._interactions[label] = self._create_interaction(label)
        return self._interactions[label]

    def _create_interaction(self, label):
        return Interaction010(label)

    def _predict(self, experience):
        """ Finds an interaction from its experience
            @return The interaction.
        """
        interaction = None
        for i in self._interactions.values():
            if i.get_experience() == experience:
                interaction = i

        if interaction is None:
            return None

        return interaction.get_result()

    def _add_or_get_experience(self, label):
        """ Creates a new experience from its label and stores it in memory.
            @param label: The experience's label
            @return The experience.
        """
        if label not in self._experiences:
            self._experiences[label] = self._create_experience(label)
        return self._experiences[label]

    def _create_experience(self, label):
        return Experiment(label)

    def _get_other_experience(self, experience):
        """ Finds an experience different from that passed in parameter.
            @param experience: The experience that we don't want
            @return The other experience.
        """
        for e in self._experiences.values():
            if e is not experience:
                return e
        else:
            return None

    def _create_or_get_result(self, label):
        """ Creates a new result from its label and stores it in memory.
            @param label: The result's label
            @return The result.
        """
        if label not in self._results:
            self._results[label] = Result(label)
        return self._results[label]

    def get_mood(self):
        return self._mood

    def set_mood(self, mood):
        self._mood = mood

    def set_previous_experience(self, previous_experience):
        self._previous_experience = previous_experience

    def get_previous_experience(self):
        return self._previous_experience

    def get_self_satisfaction_counter(self):
        return self._self_satisfaction_counter

    def set_self_satisfaction_counter(self, self_satisfaction_counter):
        self._self_satisfaction_counter = self_satisfaction_counter

    def inc_self_satisfaction_counter(self):
        self._self_satisfaction_counter += 1

    def return_result_010(self, experience):
        """ The Environment010
            E1 results in R1. E2 results in R2.
            @param experience: The current experience.
            @return The result of this experience.
        """
        if experience is self._add_or_get_experience(self.LABEL_E1):
            return self._create_or_get_result(self.LABEL_R1)
        else:
            return self._create_or_get_result(self.LABEL_R2)
