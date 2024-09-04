sequencia = input()

gamesLeft = 0
gamesRight = 0
pointsLeft, pointsRight = 0, 0
saque = 0
winner = -1
for i in sequencia:
    if i == 'Q':
        if winner == -1:
            if saque == 0:
                print(f"{gamesLeft} ({pointsLeft}*) - {gamesRight} ({pointsRight})")
            else:
                print(f"{gamesLeft} ({pointsLeft}) - {gamesRight} ({pointsRight}*)")
        else:
            if winner == 0:
                print(f"{gamesLeft} (winner) - {gamesRight}")
            else:
                print(f"{gamesLeft} - {gamesRight} (winner)")
           
    elif i == 'S':
        if saque == 0:
            pointsLeft += 1
        else:
            pointsRight += 1
    else:
        if saque == 0:
            pointsRight += 1
            saque = 1
        else:
            pointsLeft += 1
            saque = 0

    if (pointsLeft >= 5 and (pointsLeft - pointsRight) >= 2) or pointsLeft >= 10:
        gamesLeft += 1
        if(gamesLeft >= 2):
            winner = 0
        pointsLeft, pointsRight = 0, 0
        saque = 0

    elif (pointsRight >= 5 and (pointsRight - pointsLeft) >= 2) or pointsRight >= 10:
        gamesRight += 1
        if(gamesRight >= 2):
            winner = 1
        pointsLeft, pointsRight = 0, 0
        saque = 1
