
gameboard = { x : [ [y, 0] for y in "ABCDEFGH" if y != x ] for x in "ABCDEFGH"}

YOU = 1
ME = 2

def addMove(in_move, player, graph) : #takes "AB"/"BA" as a move, 0,1,2 for player
    move = sorted(in_move)
    adj_listA = graph[move[0]]
    adj_listB = graph[move[1]]
    for i in adj_listA:
        if i[0] == move[1]:
            if i[1] == 0:
                i[1] = i[1] + player
            else:
                if player == YOU:
                    print("Sorry, the move %s has already been made." % ''.join(move))
                return False
    for j in adj_listB:
        if j[0] == move[0]:
            if j[1] == 0:
                j[1] = player
            else:
                if player == YOU:
                    print("Sorry, the move %s has already been made." % ''.join(move))
                return False
    return True


def evalMove(move, player, graph) : #takes "AB"/"BA" as a move, 0,1,2 for player, and a gameboard
    value = 0
    adj_listA = graph[move[0]]
    adj_listB = graph[move[1]]
    for i in adj_listA:
        for j in adj_listB:
            if i[0] == j[0]:
                value = value + player + i[1] + j[1]
                if player == i[1] and player == j[1]:
                    return -100 # the player would lose
    return value

def chooseMove(player, graph): #alpha-beta
    best_score = -101
    best_move = ""
    temp = graph
    for key, value in temp.iteritems():
        for i in value:
            if i[1] == 0:
                possible = evalMove(''.join([key, i[0]]), player, temp)
                if possible > best_score:
                    best_move = ''.join([key, i[0]])
                    best_score = possible
                    #print(best_move, best_score)
    return best_move

def main() :
    first = raw_input("Would you like to go first? (Y/N) ")

    if first == "Y":
        me_first = False

    else:
        me_first = True

    gameOver = False

    while not gameOver:
        legal_move = False
        if me_first:
            while not legal_move:
                my_move = chooseMove(ME, gameboard)
                print "My move: ", my_move
                if (evalMove(my_move, ME, gameboard) == -100) :
                    print("I lose :(")
                    gameOver = True
                legal_move = addMove(my_move, ME, gameboard)

            legal_move = False
            while not legal_move:
                player_move = raw_input("Your move: ")

                if evalMove(player_move, YOU, gameboard) == -100 :
                    print("You lose :)")
                    gameOver = True

                legal_move = addMove(player_move, YOU, gameboard)

        else:
            while not legal_move:
                player_move = raw_input("Your move: ")
                if evalMove(player_move, YOU, gameboard) == -100 :
                    print("You lose :)")
                    gameOver = True
                legal_move = addMove(player_move, YOU, gameboard)
            legal_move = False
            while not legal_move:
                my_move = chooseMove(ME, gameboard)
                print "My move: ", my_move
                if (evalMove(my_move, ME, gameboard) == -100) :
                    print("I lose :(")
                    gameOver = True
                legal_move = addMove(my_move, ME, gameboard)
main()
