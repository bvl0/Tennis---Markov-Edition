import json
import random
import match
import numpy as np 

def win_mean_std(data, space_length):
    
    matches = []

    for i in range(space_length):
        random_index = random.randint(0, len(data)-1)
        matches.append(data[random_index])
    
    a_wins = []
    b_wins = []

    for mt in matches:
        m1 = match.match()
        m2 = match.match()
        
        m1.sets = mt['match_1']['sets']
        m1.winner = mt['match_1']['winner']

        m2.sets = mt['match_2']['sets']
        m2.winner = mt['match_2']['winner']

        if m1.winner == 0 and m2.winner == 0:
            a_wins.append(1)
        else:
            a_wins.append(0)

        if m1.winner == 1 and m2.winner == 1:
            b_wins.append(1)
        else:
            b_wins.append(0)
    
    a_wins = np.array(a_wins)
    b_wins = np.array(b_wins)

    return [(np.mean(a_wins), np.std(a_wins)), (np.mean(b_wins), np.std(b_wins))]

    #return ({"A" : str((a_wins/len(matches))*100) + "%"}, {"B": str((b_wins/len(matches))*100) + "%"})


if __name__ == "__main__":
    with open('resultados.json', 'r') as file:
        data = json.load(file)
        a_mean = 0
        a_std = 0
        b_mean = 0
        b_std = 0
        for _ in range(3000):
            mean_std = (win_mean_std(data, 3))
            a_mean = a_mean + mean_std[0][0]
            b_mean = b_mean + mean_std[1][0]
            a_std = a_std + mean_std[0][1]
            b_std = b_std + mean_std[1][1]

        print("A MEAN -> " + str(a_mean/3000) + " STD -> " + str(a_std/3000))
        print("B MEAN -> " + str(b_mean/3000) + " STD -> " + str(b_std/3000))
