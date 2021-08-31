#include <stdio.h>

#define BACKGROUND_PIXEL    0
#define IMAGE_PIXEL         1
#define COUNTED             2
#define N                   8

int maze[][8] = { {0, 0, 1, 0, 0, 0, 0, 1},
                  {1, 1, 0, 0, 0, 1, 0, 0}, 
                  {0, 0, 1, 0, 1, 0, 1, 0},
                  {0, 0, 0, 0, 0, 1, 0, 0},
                  {0, 1, 0, 1, 0, 1, 0, 0},
                  {0, 1, 0, 1, 0, 1, 0, 0},
                  {1, 0, 0, 0, 1, 1, 0, 0},
                  {0, 1, 1, 0, 0, 0, 1, 1} };

int countCells(int x, int y) {
    int count = 0;

    if(maze[x][y] == BACKGROUND_PIXEL)
        return 0;
    if(maze[x][y] == COUNTED)
        return 0;
    if(x<0 || x>=N || y<0 || y>=N)
        return 0;
    count++;
    maze[x][y] = COUNTED;

    count = count + countCells(x-1, y+1) + countCells(x-1, y) + countCells(x-1, y-1) + countCells(x, y+1) + countCells(x, y-1) + countCells(x+1, y+1) + countCells(x+1, y) + countCells(x+1, y-1);
    return count;
}

int main() {
    printf("%d\n", countCells(3, 5));
}
