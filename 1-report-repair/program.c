#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define TARGET 2020
#define MAX_SIZE 2048

int main(void)
{
    int intList[MAX_SIZE];
    int intTable[MAX_SIZE];
    int listLength = 0;
    int i;
    for(i = 0; scanf("%d\n", &intList[i]) == 1; i++) listLength++;
    for(i = 0; i < MAX_SIZE; i++) intTable[i] = 0;
    for(i = 0; i < listLength; i++) intTable[intList[i]] = 1;

    // puzzle 1
    for(i = 0; i < listLength; i++) if(intTable[TARGET - intList[i]]) break;
    printf("Puzzle 1: %d & %d sum to %d, multiply to %d\n", intList[i], TARGET - intList[i], TARGET, intList[i] * (TARGET - intList[i]));

    // puzzle 2
    int j = 0;
    int r = 0;
    for(i = 0; i < listLength; i++)
    {
        for(j = i+1; j < listLength; j++)
        {
            r = TARGET - intList[j] - intList[i];
            if(r >= 1 && r <= MAX_SIZE && intTable[r]) break;
        }
        if(r >= 1 && r <= MAX_SIZE && intTable[r]) break;
    }

    printf("Puzzle 2: %d & %d & %d sum to %d, multiply to %d\n", intList[i], intList[j], r, TARGET, intList[i] * intList[j] * r);

    return 0;
}
