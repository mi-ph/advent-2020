#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

#define MAX_LINE 4096
#define MAX_STARTING_NUMS 24

int play(int startingNums[MAX_STARTING_NUMS], int N, int dinnerTime)
{
    int *record;
    record = (int *)malloc(N * sizeof(int));
    int num, nextNum;
    for(int i = 0; i < N; i++) record[i] = 0;
    for(int t = 1; t <= dinnerTime; t++)
    {
        num = t <= N ? startingNums[t-1] : nextNum;
        nextNum = record[num] > 0 ? t - record[num] : 0;
        record[num] = t;
    }
    free(record);
    return num;
}

int main(void)
{
    int startingNums[MAX_STARTING_NUMS];
    int N;
    for(N = 0; scanf("%d,", &startingNums[N]) == 1; N++);
    printf("%d\n", play(startingNums, N, 2020));
    printf("%d\n", play(startingNums, N, 30000000));
    return 0;
}
