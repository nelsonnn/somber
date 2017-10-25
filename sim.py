
graph = { x : [ [y, 0] for y in "ABCDEFGH" if y != x ] for x in "ABCDEFGH"}

def addMove(in_move, player) : #takes "AB"/"BA" as a move, 0,1,2 for player
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
                # print(move[1]+move[0])
            else:
                if player == 2:
                    print("Sorry, the move %s has already been made.\n" % ''.join(move))
                return False
    return True


def evalMove(move, player) : #takes "AB"/"BA" as a move, 0,1,2 for player
    value = 0
    adj_listA = graph[move[0]]
    adj_listB = graph[move[1]]
    for i in adj_listA:
        for j in adj_listB:
            if i[0] == j[0]:
                print(i[0])
                # i = A-C, j = B-C
                print(i[1])
                print(j[1])
                value = value + player + i[1] + j[1]
    return value

def main() :
    addMove("BC", 1)
    addMove("AB", 2)
    print(evalMove("AC",1))


main()
