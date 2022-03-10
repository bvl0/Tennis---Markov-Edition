import random
def game(p, tiebrake, arquivo):
    points = [0,0]

    limit = 7 if tiebrake else 4
    gameCount = 1
    
    arquivo.write("        ")
    while max(points) < limit or (max(points) - min(points)) <= 1:
        if random.random() <= p:
            points[0] += 1
        else:
            points[1] +=1
        
        arquivo.write(str(points) + " ")
    
    #print("points = " + str(points))
    arquivo.write("\n")
    if points[0] > points[1]:
        return 0
    else:
        return 1

def set(p, arquivo):
    games = [0,0]
    gameCount = 1
    while max(games) < 7:
        if max(games) == 6 and max(games) - min(games) >=2:
            break
        
        if games[0] == 6 and games[1] == 6:
            #print("tiebrake")
            tiebrake = True
        else:
            tiebrake = False

        arquivo.write("      game " + str(gameCount) + ":\n")
        winner = game(p, tiebrake, arquivo)
        games[winner] += 1
        gameCount += 1
    
    #print("games = " + str(games))
    arquivo.write("    result: " + str(games) + "\n")
    if games[0] > games[1]:
        return 0
    else:
        return 1

def match(p, arquivo):
    sets = [0,0]
    setCount = 1

    while max(sets) < 2:
        arquivo.write("    set " + str(setCount) + ":\n")
        winner = set(p, arquivo)
        sets[winner] += 1
        setCount += 1

    if sets[0] > sets[1]:
        return 0
    else:
        return 1

def simulation(p1, p2 , n):
    matchs = [0,0]
    with open('resultados.txt', 'w') as arquivo:
        arquivo.write("partida 1:\n")
        for x in range (n):
            arquivo.write("  match " + str(x+1) + ":\n")
            winner = match(p1, arquivo)
            matchs[winner] += 1
            #print("partida :" + str(x+1) + " vencedor: " + str(match(p)))
        
        arquivo.write("resultados grupo 1 : " + str(matchs) + "\n")
        
        arquivo.write("partida 2:\n")
        matchs = [0,0]
        for x in range (n):
            arquivo.write("  match " + str(x+1) + ":\n")
            winner = match(p2, arquivo)
            matchs[winner] += 1
            #print("partida :" + str(x+1) + " vencedor: " + str(match(p)))

        arquivo.write("resultados grupo 2 : " + str(matchs) + "\n")

simulation(0.7, 0.5, 30)