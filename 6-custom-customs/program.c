#include <stdio.h>

#define MAX_LINE 4096

int main(void) {
    char line[MAX_LINE];
    int oneSaidYes = 0;
    int allSaidYes = 0;
    int questions[26];
    int N = 0;

    for(int i = 0; i < 26; i++) questions[i] = 0;
    while(fgets(line, MAX_LINE, stdin))
    {
        if(line[0] == '\n') {
            for(int i = 0; i < 26; i++)
            {
                oneSaidYes += (questions[i] > 0);
                allSaidYes += (questions[i] == N);
                questions[i] = 0;
            }
            N = 0;
        } else {
            for(int i = 0; line[i] != '\n'; i++)
            {
                questions[line[i] - 'a'] += 1;
            }
            N++;
        }
    }
    for(int i = 0; i < 26; i++)
    {
        oneSaidYes += (questions[i] > 0);
        allSaidYes += (questions[i] == N);
        questions[i] = 0;
    }
    printf("At least one said yes: %d\n", oneSaidYes);
    printf("All said yes: %d\n", allSaidYes);
    return 0;
}
