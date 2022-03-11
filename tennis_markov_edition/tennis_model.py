from markov_chain import chain
from markov_chain import state

# defines a tennis model class


class tennis_model:
    def __init__(self, p):
        self.p = p  # probability of A winning a point
        self.q = 1 - p

        states = [
            state('0-0'),  # 0
            state('15-love'),  # 1
            state('30-love'),  # 2
            state('40-love'),  # 3
            state('love-15'),  # 4
            state('love-30'),  # 5
            state('love-40'),  # 6
            state('15-15'),  # 7
            state('15-30'),  # 8
            state('15-40'),  # 9
            state('30-15'),  # 10
            state('40-15'),  # 11
            state('deuce'),  # 12
            state('adv. A'),  # 13
            state('adv. B'),  # 14
            state('A-win'),  # 15
            state('B-win'),  # 16
        ]

        states[0].add_transition(states[1])
        states[0].add_transition(states[4])

        states[1].add_transition(states[2])
        states[1].add_transition(states[7])

        states[2].add_transition(states[3])
        states[2].add_transition(states[10])

        states[3].add_transition(states[15])
        states[3].add_transition(states[11])

        states[4].add_transition(states[7])
        states[4].add_transition(states[5])

        states[5].add_transition(states[8])
        states[5].add_transition(states[6])

        states[6].add_transition(states[9])
        states[6].add_transition(states[16])

        states[7].add_transition(states[10])
        states[7].add_transition(states[8])

        states[8].add_transition(states[12])
        states[8].add_transition(states[9])

        states[9].add_transition(states[14])
        states[9].add_transition(states[16])

        states[10].add_transition(states[11])
        states[10].add_transition(states[12])

        states[11].add_transition(states[15])
        states[11].add_transition(states[13])

        states[12].add_transition(states[13])
        states[12].add_transition(states[14])

        states[13].add_transition(states[15])
        states[13].add_transition(states[12])

        states[14].add_transition(states[12])
        states[14].add_transition(states[16])

        self.markov_chain = chain(states, self.p)
        self.current_state = states[0]
        self.points = (0, 0)
        self.sets = []
        self.match_winner = None

    def change_state(self):
        state = self.markov_chain.next_state(self.current_state)
        self.current_state = state[0]
        if (state[1] == 0):
            self.points = (self.points[0]+1, self.points[1])
        else:
            self.points = (self.points[0], self.points[1]+1)

    def is_final_state(self):
        return self.current_state.transitions == []

    def get_winner(self):
        if self.current_state.name == 'A-win':
            return 0
        else:
            return 1

    def get_points(self):
        return self.points

    def restart_states(self):
        self.current_state = self.markov_chain.get_states()[0]
        self.points = (0, 0)

    def push_set(self):
        self.sets.append([])

    def add_point(self):
        self.sets[-1].append(self.points)
    
    def define_set_winner(self, winner):
        self.sets[-1].append({"winner":winner})

    def define_match_winner(self, winner):
        self.match_winner = winner
    
    def get_match_info(self):
        return dict({"sets":self.sets, "winner":self.match_winner})