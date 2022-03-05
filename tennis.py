import random
def game(p, tiebrake):
    points = [0,0]

    limit = 7 if tiebrake else 4
    
    while max(points) < limit or (max(points) - min(points)) <= 1:
        if random.random() <= p:
            points[0] += 1
        else:
            points[1] +=1
    
    print("points = " + str(points))
    
    if points[0] > points[1]:
        return 0
    else:
        return 1

def set(p):
    games = [0,0]

    while max(games) < 7:
        if max(games) == 6 and max(games) - min(games) >=2:
            break
        
        if games[0] == 6 and games[1] == 6:
            print("tiebrake")
            tiebrake = True
        else:
            tiebrake = False

        winner = game(p, tiebrake)
        games[winner] += 1
    
    print("games = " + str(games))
    if games[0] > games[1]:
        return 0
    else:
        return 1


def match(p):
    sets = [0,0]

    while max(sets) < 2:
        winner = set(p)
        sets[winner] += 1

    print(sets)





match(0.5)