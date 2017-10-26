
gameboard = { x : [ [y, 0] for y in "ABCDEFGH" if y != x ] for x in "ABCDEFGH"}

RED = 1
BLUE = 2

def addMove(in_move, player, graph) : #takes "AB"/"BA" as a move, 0,1,2 for player
    move = sorted(in_move)
    adj_listA = graph[move[0]]
    adj_listB = graph[move[1]]
    for i in adj_listA:
        if i[0] == move[1]:
            if i[1] == 0:
                i[1] = i[1] + player
            else:
                if player == 2:
                    print("Sorry, the move %s has already been made.\n" % ''.join(move))
                return False
    for j in adj_listB:
        if j[0] == move[0]:
            if j[1] == 0:
                j[1] = player
            else:
                if player == 2:
                    print("Sorry, the move %s has already been made.\n" % ''.join(move))
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
                    print(best_move, best_score)
    return best_move

def main() :
    addMove("HG", 1, gameboard)
    addMove("HF", 2, gameboard)
    print(chooseMove(1, gameboard))


main()
