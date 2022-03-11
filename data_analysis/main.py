import json
import random
import match
import numpy as np
from tabulate import tabulate


def get_mean_std(data, space_length):

    matches = []

    for i in range(space_length):
        random_index = random.randint(0, len(data)-1)
        matches.append(data[random_index])

    a_1_wins = []
    b_1_wins = []
    a_2_wins = []
    b_2_wins = []

    for mt in matches:
        m1 = match.match()
        m2 = match.match()

        m1.sets = mt['match_1']['sets']
        m1.winner = mt['match_1']['winner']

        m2.sets = mt['match_2']['sets']
        m2.winner = mt['match_2']['winner']

        if m1.winner == 0:
            a_1_wins.append(1)
            b_1_wins.append(0)
        else:
            b_1_wins.append(1)
            a_1_wins.append(0)
        
        if m2.winner == 0:
            a_2_wins.append(1)
            b_2_wins.append(0)
        else:
            b_2_wins.append(1)
            a_2_wins.append(0)




    a_1_wins = np.array(a_1_wins)
    b_1_wins = np.array(b_1_wins)
    a_2_wins = np.array(a_2_wins)
    b_2_wins = np.array(b_2_wins)

    return [
        (np.mean(a_1_wins), np.std(a_1_wins)),
        (np.mean(b_1_wins), np.std(b_1_wins)),
        (np.mean(a_2_wins), np.std(a_2_wins)),
        (np.mean(b_2_wins), np.std(b_2_wins))
    ]


def sets_games_points(data, space_length):
    sets_a = []
    games_a = []
    points_a = []

    sets_b = []
    games_b = []
    points_b = []

    matches = []

    for i in range(space_length):
        random_index = random.randint(0, len(data)-1)
        matches.append(data[random_index])

    for mt in matches:
        m1 = match.match()
        m2 = match.match()

        m1.sets = mt['match_1']['sets']
        m1.winner = mt['match_1']['winner']

        m2.sets = mt['match_2']['sets']
        m2.winner = mt['match_2']['winner']

        sets_a.append(len(m1.sets))
        games_a.append(sum(len(s) for s in m1.sets) - len(m1.sets))
        points_a.append(list(map(lambda x: x[:-1], m1.sets)))
        
        sets_b.append(len(m2.sets))
        games_b.append(sum(len(s) for s in m2.sets) - len(m2.sets))
        points_b.append(list(map(lambda x: x[:-1], m2.sets)))


    points_a = sum(sum(sum(points_a, []), [],), [])
    points_b = sum(sum(sum(points_b, []), [],), [])

    return [(np.mean(sets_a), np.std(sets_a)), (np.mean(games_a), np.std(games_a)), (np.mean(points_a), np.std(points_a)), (np.mean(sets_b), np.std(sets_b)), (np.mean(games_b), np.std(games_b)), (np.mean(points_b), np.std(points_b))]


def full_analysis(data, space_length, reps):
    a_1_mean = 0
    a_1_std = 0
    b_1_mean = 0
    b_1_std = 0
    a_2_mean = 0
    a_2_std = 0
    b_2_mean = 0
    b_2_std = 0
    sets_a_mean = 0
    sets_a_std = 0
    games_a_mean = 0
    games_a_std = 0
    points_a_mean = 0
    points_a_std = 0
    sets_b_mean = 0
    sets_b_std = 0
    games_b_mean = 0
    games_b_std = 0
    points_b_mean = 0
    points_b_std = 0

    for _ in range(reps):
        ab_mean_std = (get_mean_std(data, space_length))
        a_1_mean = a_1_mean + ab_mean_std[0][0]
        b_1_mean = b_1_mean + ab_mean_std[1][0]
        a_1_std = a_1_std + ab_mean_std[0][1]
        b_1_std = b_1_std + ab_mean_std[1][1]
        a_2_mean = a_2_mean + ab_mean_std[2][0]
        b_2_mean = b_2_mean + ab_mean_std[3][0]
        a_2_std = a_2_std + ab_mean_std[2][1]
        b_2_std = b_2_std + ab_mean_std[3][1]

        sgp_mean_std = sets_games_points(data, space_length)
        sets_a_mean = sets_a_mean + sgp_mean_std[0][0]
        games_a_mean = games_a_mean + sgp_mean_std[1][0]
        points_a_mean = points_a_mean + sgp_mean_std[2][0]
        sets_a_std = sets_a_std + sgp_mean_std[0][1]
        games_a_std = games_a_std + sgp_mean_std[1][1]
        points_a_std = points_a_std + sgp_mean_std[2][1]
        sets_b_mean = sets_b_mean + sgp_mean_std[3][0]
        games_b_mean = games_b_mean + sgp_mean_std[4][0]
        points_b_mean = points_b_mean + sgp_mean_std[5][0]
        sets_b_std = sets_b_std + sgp_mean_std[3][1]
        games_b_std = games_b_std + sgp_mean_std[4][1]
        points_b_std = points_b_std + sgp_mean_std[5][1]
    a_1_mean = a_1_mean / reps
    b_1_mean = b_1_mean / reps
    a_2_mean = a_2_mean / reps
    b_2_mean = b_2_mean / reps
    a_1_std = a_1_std / reps
    b_1_std = b_1_std / reps
    a_2_std = a_2_std / reps
    b_2_std = b_2_std / reps
    sets_a_mean = sets_a_mean / reps
    games_a_mean = games_a_mean / reps
    points_a_mean = points_a_mean / reps
    sets_a_std = sets_a_std / reps
    games_a_std = games_a_std / reps
    points_a_std = points_a_std / reps
    sets_b_mean = sets_b_mean / reps
    games_b_mean = games_b_mean / reps
    points_b_mean = points_b_mean / reps
    sets_b_std = sets_b_std / reps
    games_b_std = games_b_std / reps
    points_b_std = points_b_std / reps

    data_1 = [
        ['A wins', a_1_mean, a_1_std, a_2_mean, a_2_std],
        ['B wins', b_1_mean, b_1_std, b_2_mean, b_2_std],
        ['Sets', sets_a_mean, sets_a_std, sets_b_mean, sets_b_std],
        ['Games', games_a_mean, games_a_std, games_b_mean, games_b_std],
        ['Points', points_a_mean, points_a_std, points_b_mean, points_b_std],
    ]

    print(tabulate(data_1, headers=['Label', 'Mean M1', 'Std M1', 'Mean M2', 'Std M2'], tablefmt='orgtbl'))


if __name__ == "__main__":
    with open('resultados.json', 'r') as file:
        data = json.load(file)
        print('\nWith 3 Samples\n')
        full_analysis(data, 3, 3000)
        print('\nWith 10 samples\n')
        full_analysis(data, 10, 3000)
        print('\n')
