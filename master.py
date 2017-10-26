import itertools
from random import randint

colors = "RBOW"
canidates = [ p for p in itertools.product(colors, repeat = 3) ] # all possible guesses
# canidates_O = { x : [y for y in colors] for x in range(1,4) }
def main():
    gameOver = False
    while not gameOver:

        guess = canidates[randint(0,len(canidates)-1)]

        color0 = guess[0]
        color1 = guess[1]
        color2 = guess[2]

        response = raw_input(''.join(guess) + "   Your answer: ")

        if response:
            if response == "XXX":
                gameOver = True
            if response == "O": # none in right spots, but one right color
                canidates.remove(guess)
                for poss in canidates:
                    has0 = color0 in poss
                    has1 = color1 in poss
                    has2 = color2 in poss
                    if not ( ( has0 and (not has1) and (not has2) ) or ( has1 and (not has0) and (not has2) ) or ( has2 and (not has0) and (not has1) ) ) :
                        print "Removed: " , ''.join(poss)
                        canidates.remove(poss)
            if response == "OO":
                canidates.remove(guess)
                for poss in canidates:
                    has0 = color0 in poss
                    has1 = color1 in poss
                    has2 = color2 in poss
                    if not( ( has0 and has1 and (not has2) ) or ( has0 and has2 and (not has1) ) or ( has2 and has1 and (not has0) ) ):
                        print "Removed: " , ''.join(poss)
                        canidates.remove(poss)
            if response == "OOO":
                canidates.remove(guess)
                for poss in canidates:
                    has0 = color0 in poss
                    has1 = color1 in poss
                    has2 = color2 in poss
                    if not( has0 and has1 and has2 ):
                        print "Removed: " , ''.join(poss)
                        canidates.remove(poss)

            # TODO Implement "OX" rule
            
            if response == "X":
                canidates.remove(guess)
                for poss in canidates:
                    if not (poss[0] == color0 or poss[1] == color1 or poss[2] == color2):
                        print "Removed: " , ''.join(poss)
                        canidates.remove(poss)
            if response == "XX":
                canidates.remove(guess)
                for poss in canidates:
                    if not( (color0 == poss[0] and color1 == poss[1]) or (color0 == poss[0] and color2 == poss[2]) or (color1 == poss[1] and color2 == poss[2]) ):
                        print "Removed: " , ''.join(poss)
                        canidates.remove(poss)

        print len(canidates), "possible right answers remaining"



main()
