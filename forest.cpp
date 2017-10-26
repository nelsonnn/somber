#include<iostream>
#include<string>
#include<queue>
#define MAX true
#define MIN false

struct node {
  node() {};
  bool full = false;
  int key;
  node* left = new node();
  node* middle = new node();
  node* right = new node();

};

int maximum( int a, int b, int c )
{
  int max = ( a < b ) ? b : a;
  return ( ( max < c ) ? c : max );
}

int minimum( int a, int b, int c )
{
  int max = ( a > b ) ? b : a;
  return ( ( max > c ) ? c : max );
}

class tree {
public:
  tree() {};
  void insert(node* root, int depth, int i) {
    if (depth < 4) {
      if (!root->left->full) {
        insert(root->left, depth+1, i);
      } else if (!root->middle->full) {
        insert(root->middle, depth+1, i);
      } else if (!root->right->full) {
        insert(root->right, depth+1, i);
      } else root->full = true;
    } else {
      root->key = i;
      root->full = true;
      delete root->left;
      delete root->middle;
      delete root->right;
    }
  }

  node* root = new node();

  int minimax(node* root, bool player, int depth){
    if (player) { //MAX
      if (depth < 3) {
        return maximum(minimax(root->left, !player, depth+1), minimax(root->middle, !player, depth+1), minimax(root->right, !player, depth+1));
      } else return maximum(root->left->key, root->middle->key, root->right->key);
    } else {
      if (depth < 3) {
        return minimum(minimax(root->left, !player, depth+1), minimax(root->middle, !player, depth+1), minimax(root->right, !player, depth+1));
      } else return minimum(root->left->key, root->middle->key, root->right->key);

    }

  }
};

int main(int argc, char const *argv[]) {
  int data[81] = {
    8,3,7,
    2,5,9,
    5,3,8,
    2,5,7,
    9,4,8,
    6,3,2,
    4,9,5,
    1,7,2,
    2,4,6,
    1,4,7,
    8,4,2,
    5,7,8,
    2,4,6,
    9,5,6,
    1,0,2,
    4,5,3,
    9,2,7,
    3,1,7,
    9,5,6,
    4,0,1,
    3,4,5,
    1,2,3,
    7,3,4,
    4,3,2,
    8,2,7,
    1,9,3,
    2,7,3,
  };
  tree foo;
  for (int i = 0; i < 81; i++){
    foo.insert(foo.root, 0, data[i]);
  }
  std::cout << "Helo world" << foo.minimax(foo.root, MAX, 0);
  return 0;
}
