#include <stdio.h>

#define MAX_LINE 4096

int main(void) {
    int filledSeats[1024];
    char line[MAX_LINE];
    int biggestId = 0;

    for(int i = 0; i < 1024; i++) filledSeats[i] = 0;
    while(fgets(line, MAX_LINE, stdin))
    {
        int row = 0;
        int multiplier = 64;
        for(int i = 0; i < 7; i++) {
            if(line[i] == 'B') row += multiplier;
            multiplier /= 2;
        }
        int col = 0;
        multiplier = 4;
        for(int i = 7; i < 10; i++) {
            if(line[i] == 'R') col += multiplier;
            multiplier /= 2;
        }
        int id = 8 * row + col;
        if (id > biggestId) biggestId = id;
        filledSeats[id] = 1;
    }
    printf("%d is the biggest ID.\n", biggestId);
    for(int i = 1; i < 1023; i++)
    {
        if(filledSeats[i] == 0 && filledSeats[i+1] && filledSeats[i-1]) printf("%d is empty\n", i);
    }

    return 0;
}
