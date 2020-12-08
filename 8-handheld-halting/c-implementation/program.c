#include <stdio.h>

#define OP_NOP 0
#define OP_JMP 1
#define OP_ACC 2

#define MAX_STRING 64
#define MAX_PMEM 2048

int run(int *acc, int *param, int *opCode, int programLength)
{
    int errorCode = 0;
    int pc = 0;
    int visited[MAX_PMEM];
    for(int i = 0; i < MAX_PMEM; i++) visited[i] = 0;
    while(errorCode == 0 && pc < programLength)
    {
        visited[pc] = 1;
        if(opCode[pc] == OP_ACC) *acc += param[pc];
        if(opCode[pc] == OP_JMP) pc += (param[pc] - 1);
        pc++;
        if(visited[pc]) errorCode = 1;
    }
    return errorCode;
}

int main(void)
{
    char op[MAX_STRING];
    int param[MAX_PMEM];
    int opCode[MAX_PMEM];
    int programLength = 0;
    int acc;

    for(int i = 0; scanf("%s %d\n", op, &param[i]) == 2; i++)
    {
        if(op[0] == 'n') opCode[i] = OP_NOP;
        if(op[0] == 'j') opCode[i] = OP_JMP;
        if(op[0] == 'a') opCode[i] = OP_ACC;
        programLength++;
    }

    // puzzle 1
    acc = 0;
    run(&acc, param, opCode, programLength);
    printf("Puzzle 1: %d\n", acc);

    // puzzle 2
    for(int i = 0; i < programLength; i++)
    {
        acc = 0;
        if (opCode[i] == OP_NOP) opCode[i] = OP_JMP;
        else if (opCode[i] == OP_JMP) opCode[i] = OP_NOP;
        if (!run(&acc, param, opCode, programLength))
        {
            printf("Puzzle 2: %d\n", acc);
            break;
        }
        if (opCode[i] == OP_NOP) opCode[i] = OP_JMP;
        else if (opCode[i] == OP_JMP) opCode[i] = OP_NOP;
    }

    return 0;
}
