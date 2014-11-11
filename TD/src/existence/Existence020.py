# Sibling packages
from coupling.interaction import Interaction020

# Current package
from existence import Existence010


class Existence020(Existence010):
    """ An Existence020 is a sort of Existence010 in which each Interaction has
        a predefined Valence.
        When a given Experience is performed and a given Result is obtained,
        the corresponding Interaction is considered enacted.
        The Existence020 is PLEASED when the enacted Interaction has a positive
        or null Valence, and PAINED otherwise.
        An Existence020 is still a single entity rather than being split into
        an explicit Agent and Environment.
        An Existence020 demonstrates a rudimentary decisional mechanism and a
        rudimentary learning mechanism.
        It learns to choose the Experience that induces an Interaction that has
        a positive valence.
        Try to change the Valences of interactions and the method
        giveResult(experience)
        and observe that the Existence020 still learns to enact interactions
        that have positive valences.
    """

    def _init_existence(self):
        e1 = self._add_or_get_experience(self.LABEL_E1)
        e2 = self._add_or_get_experience(self.LABEL_E2)
        r1 = self._create_or_get_result(self.LABEL_R1)
        r2 = self._create_or_get_result(self.LABEL_R2)

        self._add_or_get_primitive_interaction(e1, r1, -1)
        self._add_or_get_primitive_interaction(e1, r2, 1)
        self._add_or_get_primitive_interaction(e2, r1, -1)
        self._add_or_get_primitive_interaction(e2, r2, 1)

        self.set_previous_experience(e1)

    def step(self):
        experience = self.get_previous_experience()
        if self.get_mood() in [self.Mood.PAINED, self.Mood.BORED]:
            experience = self._get_other_experience(experience)
            self.set_self_satisfaction_counter(0)
        else:
            # Do, one more time, the same experiment
            self.inc_self_satisfaction_counter()

        result = self.return_result_010(experience)

        enacted_interaction = \
            self._add_or_get_primitive_interaction(experience, result)

        if enacted_interaction.get_valence() >= 0:
            self.set_mood(self.Mood.PLEASED)
        else:
            self.set_mood(self.Mood.PAINED)

        if self.get_self_satisfaction_counter() >= self.BOREDOME_LEVEL:
            self.set_mood(self.Mood.BORED)

        self.set_previous_experience(experience)

        return '{0}{1} {2}'.format(experience.get_label(),
                                   result.get_label(),
                                   self.get_mood())

    def _add_or_get_primitive_interaction(self, experience, result,
                                          valence=None):
        """ Create an interaction as a tuple <experience, result>.
            @param experience: The experience.
            @param result: The result.
            @param valence: the interaction's valence
            @return The created interaction
        """
        interaction_label = self._get_primitive_interaction_label(experience,
                                                                  result)
        if valence is not None and interaction_label not in self._interactions:
            interaction = self._create_interaction(interaction_label)
            interaction.set_experience(experience)
            interaction.set_result(result)
            interaction.set_valence(valence)
            self._interactions[interaction_label] = interaction
        return self._interactions[interaction_label]

    def _create_interaction(self, label):
        return Interaction020(label)

    def _get_interaction(self, label):
        return self._interactions[label]



