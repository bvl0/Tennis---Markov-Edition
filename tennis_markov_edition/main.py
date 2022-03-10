import tennis_model
import json

def game(model):
    while(not model.is_final_state()):
        model.change_state()

    winner = model.get_winner()
    model.add_point()
    model.restart_states()

    return winner

def set(model):
    games = [0,0]
    gameCount = 1
    model.push_set()
    while max(games) < 7:
        if max(games) == 6 and max(games) - min(games) >=2:
            break

        winner = game(model)
        games[winner] += 1
        gameCount += 1
    
    if games[0] > games[1]:
        model.define_set_winner(0)
        return 0
    else:
        model.define_set_winner(1)
        return 1


def match(model):
    sets = [0, 0]
    setCount = 0
    while max(sets) < 2:
        winner = set(model)
        sets[winner] += 1
        setCount += 1

    if sets[0] > sets[1]:
        model.define_match_winner(0)
        return 0
    else:
        model.define_match_winner(1)
        return 1


if __name__ == "__main__":
    n = 30
    with open('resultados.json', 'w') as file:
        data = []
        for _ in range(n):
            model1 = tennis_model.tennis_model(0.7)
            model2 = tennis_model.tennis_model(0.5)

            match(model1)
            match(model2)

            matches = {
                'match_1': model1.get_match_info(),
                'match_2': model2.get_match_info()
            }
            data.append(matches)

        file.write(json.dumps(data))
        file.close()
