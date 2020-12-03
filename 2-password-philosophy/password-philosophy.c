#include <stdio.h>

#define DEBUG 0

int schemeOne(int countLow, int countHigh, char countChar, char *inputBuffer)
{
    int count = 0;
    for(int i = 0; inputBuffer[i] != '\0'; i++)
    {
        if(inputBuffer[i] == countChar) count++;
    }
    if(count >= countLow && count <= countHigh)
    {
        if(DEBUG) printf("Input: %s needs %d to %d of %c. Success with %d.\n", inputBuffer, countLow, countHigh, countChar, count);
        return 1;
    } else {
        if(DEBUG) printf("Input: %s needs %d to %d of %c. Failure with %d.\n", inputBuffer, countLow, countHigh, countChar, count);
        return 0;
    }
}

int schemeTwo(int countLow, int countHigh, char countChar, char *inputBuffer)
{
    int conditionOne = 2;
    int conditionTwo = 2;
    for(int i = 0; inputBuffer[i] != '\0'; i++)
    {
        if(i + 1== countLow) conditionOne = inputBuffer[i] == countChar;
        if(i + 1== countHigh) conditionTwo = inputBuffer[i] == countChar;
    }
    return conditionOne + conditionTwo == 1;
}

int main(void)
{
    char inputBuffer[128];
    char countChar;
    int countLow, countHigh;

    int validPasswordsScheme1 = 0;
    int validPasswordsScheme2 = 0;
    while(scanf("%d-%d %c: %s\n", &countLow, &countHigh, &countChar, inputBuffer) == 4)
    {
        validPasswordsScheme1 += schemeOne(countLow, countHigh, countChar, inputBuffer);
        validPasswordsScheme2 += schemeTwo(countLow, countHigh, countChar, inputBuffer);
    }
    printf("%d valid passwords in scheme 1\n", validPasswordsScheme1);
    printf("%d valid passwords in scheme 2\n", validPasswordsScheme2);
    return 0;
}
