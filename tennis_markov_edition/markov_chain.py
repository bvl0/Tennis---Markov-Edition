import random

# defines a Markov chain class
# p is the probability of A winning a point
# q is the probability of B winning a point


class chain:
    def __init__(self, states, p):
        self.states = states
        self.p = p
        self.q = 1 - p

    def get_states(self):
        return self.states

    def next_state(self, atual):
        if random.random() <= self.p:
            return (atual.get_transitions()[0], 0)
        else:
            return (atual.get_transitions()[1], 1)

# defines a state class
# a state can be interpreted as a node in a directed graph
# transitions are the adjacent vertices of the node


class state:
    def __init__(self, name):
        self.name = name
        self.transitions = []

    # elements must be added in order (first A, then B)
    def add_transition(self, transition):
        self.transitions.append(transition)

    def get_transitions(self):
        return self.transitions
