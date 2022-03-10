import json
import random
import match

def win_mean(data, space_length):
    
    matches = []

    for i in range(space_length):
        random_index = random.randint(0, len(data)-1)
        matches.append(data[random_index])
    
    for mt in matches:

        m1 = match.match()
        m2 = match.match()
        m1.sets = mt['match_1']['sets']
        m2.sets = mt['match_1']['sets']

        print(m1.sets)
        print(m2.sets)


if __name__ == "__main__":
    with open('resultados.json', 'r') as file:
        data = json.load(file)
        win_mean(data, 3)