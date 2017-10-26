#include<string.h>
#include<iostream>
#include<vector>

#define NONE 0
#define RED 1
#define BLUE 2

using namespace std;

class Move {
public:
    Move(string in_a, string in_b, int c): color(c) {
        if (in_a < in_b) {  //Keep the Moves alphabetically
            a = in_a;
            b = in_b;
        } else {
            a = in_b;
            b = in_a;
        }
    }
    Move(string move, int c): color(c) {
        std::sort(move.begin(),move.end());
        a = move.substr(0,1);
        b = move.substr(1,1);
    }
    Move() {}; // dfault

    string toStr() {
        return a+b;
    }
    string a;
    string b;
    int color;
};

struct triangle {
    // triangle(string tri, int* colors) {
    //     // AB AC BC RED NONE BLUE
    //     Move* a = new Move(tri.substr(0,2), colors[0]);
    //     Move* b = new Move(tri.substr(0,1),tri.substr(2,1), colors[1]);
    //     Move* c = new Move(tri.substr(1,2), colors[2]);
    //     value = a->color + b->color + c->color;
    // }
    triangle(move* in_a, move* in_b, move* in_c): a(in_a), b(in_b), c(in_c), value(a->color + b->color + c->color) {};
    Move* a;
    Move* b;
    Move* c;
    int value;
};

class gameState {

    public:
        gameState(gameState* prev, Move next): nodes("ABCDEFGH") {  // Constructor for creating next gameboard
            taken = prev->taken;
            bool duplicate = false;
            for (int i = 0; i < taken.size(); i++) { // MAYBE DO THIS OUTSIDE THE const
                if (taken[i].toStr() == next.toStr()) duplicate = true;
            }
            if (!duplicate) taken.push_back(next);
        }

        gameState(): nodes("ABCDEFGH"){}; //dfault Constructor

        void printMoves() {
            for (int i = 0; i < taken.size(); i++) {
                std::cout << taken[i].toStr() << '\n';
            }
        }

        int evalTri(Move a) {
            int sum = 0;
            for (int i = 0; i < strlen(nodes); i++) {
                size_t found = a.toStr().find(nodes[i]);
                if (found == string::npos) {

                }
            }
        }
    private:
        string nodes;
        std::vector<Move> taken;
};

int main(int argc, char const *argv[]) {
    /* code */
    Move a("B","A", RED);
    Move b("CA", BLUE);
    gameState* game = new gameState();
    gameState* game2 = new gameState(game, a);
    gameState* game3 = new gameState(game2, b);
    game3->printMoves();
    // game2->printMoves();
    return 0;
}
