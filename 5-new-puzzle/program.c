#include <stdio.h>

#define MAX_LINE 4096

int main(void) {
    char line[MAX_LINE];
    int biggestId = 0;
    int filledSeats[1024];

    for(int i = 0; i < 1024; i++) filledSeats[i] = 0;
    while(fgets(line, MAX_LINE, stdin))
    {
        int id = 0;
        int multiplier = 512;
        for(int i = 0; i < 10; i++) {
            if(line[i] == 'B' || line[i] == 'R') id += multiplier;
            multiplier /= 2;
        }
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
