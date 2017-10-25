#include<string.h>
#include<iostream>
#include<vector>

#define NONE 0
#define RED 1
#define BLUE 2

using namespace std;

struct move {
    move(char in_a, char in_b, int c): color(c) {
        if (in_a < in_b) {  //Keep the moves alphabetically
            a = in_a;
            b = in_b;
        } else {
            a = in_b;
            b = in_a;
        }
    }
    char a;
    char b;
    int color;
}

struct triangle {
    move a;
    move b;
    move c;
}

class gameState {

    public:
        gameState(gameState* prev, move next, int color){
            taken = prev->taken;
            bool duplicate = false;
            for (int i = 0; i < taken.size(); i++) {
                if (taken[i].a == next.a && taken[i].b == next.b) duplicate = true;
            }
            if (!duplicate) taken.push_back(next);
        }
    private:
        char nodes[] = {"A", "B", "C", "D", "E", "F", "G", "H"};
        std::vector<move> taken;
}
