#include <stdio.h>

#define MAX_HEIGHT 4096
#define WIDTH 31

int run(char lines[MAX_HEIGHT][WIDTH], int height, int right, int down)
{
    int row = down;
    int col = right % WIDTH;
    int hits = 0;
    while(row < height) {
        if(lines[row][col] == '#') hits++;
        col = (col + right) % WIDTH;
        row = row + down;
    }
    return hits;
}

int main(void)
{
    char lines[MAX_HEIGHT][WIDTH];
    int height = 0;

    while(scanf("%s\n", lines[height]) == 1) height++;

    // puzzle 1
    printf("Puzzle 1 Answer: %d\n", run(lines, height, 3, 1));

    // puzzle 2
    int product = 1;
    product *= run(lines, height, 1, 1);
    product *= run(lines, height, 3, 1);
    product *= run(lines, height, 5, 1);
    product *= run(lines, height, 7, 1);
    product *= run(lines, height, 1, 2);

    printf("Puzzle 2 Answer: %d\n", product);
    return 0;
}
