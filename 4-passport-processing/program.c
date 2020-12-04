#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_LINE 4096

int main(void)
{
    char line[MAX_LINE];

    char field[4];
    char value[MAX_LINE];

    int numPassportsValid = 0;
    int numPassportsWithAllRequiredFields = 0;
    int hasField[7] = {0, 0, 0, 0, 0, 0, 0};
    int isValid[7] = {0, 0, 0, 0, 0, 0, 0};

    int i, j;

    while(fgets(line, MAX_LINE, stdin))
    {
        for(i = 0; line[i] != '\0'; i++)
        {
            if(line[i] == ':')
            {
                int identifierIndex = i;
                line[i] = '\0';
                strcpy(field, &line[identifierIndex-3]);

                for(; line[i] != ' ' && line[i] != '\n'; i++);
                line[i] = '\0';
                strcpy(value, &line[identifierIndex+1]);

                if(!strcmp(field, "byr"))
                {
                    hasField[0] = 1;
                    int numDigits = 0;
                    for(j = 0; value[j] != '\0' && value[j] >= '0' && value[j] <= '9'; j++) numDigits++;
                    if(value[j] == '\0' && numDigits == 4)
                    {
                        int birthYear = atoi(value);
                        if(birthYear >= 1920 && birthYear <= 2002) isValid[0] = 1;
                    }
                } else if(!strcmp(field, "iyr")) {
                    hasField[1] = 1;
                    int numDigits = 0;
                    for(j = 0; value[j] != '\0' && value[j] >= '0' && value[j] <= '9'; j++) numDigits++;
                    if(value[j] == '\0' && numDigits == 4)
                    {
                        int issueYear = atoi(value);
                        if(issueYear >= 2010 && issueYear <= 2020) isValid[1] = 1;
                    }
                } else if(!strcmp(field, "eyr")) {
                    hasField[2] = 1;
                    int numDigits = 0;
                    for(j = 0; value[j] != '\0' && value[j] >= '0' && value[j] <= '9'; j++) numDigits++;
                    if(value[j] == '\0' && numDigits == 4)
                    {
                        int expirationYear = atoi(value);
                        if(expirationYear >= 2020 && expirationYear <= 2030) isValid[2] = 1;
                    }
                } else if(!strcmp(field, "hgt")) {
                    hasField[3] = 1;
                    for(j = 0; value[j] != '\0' && value[j] >= '0' && value[j] <= '9'; j++);
                    if(!strcmp(&value[j], "cm") && j != 0)
                    {
                        value[j] = '\0';
                        int height = atoi(value);
                        if(height >= 150 && height <= 193) isValid[3] = 1;
                    }
                    if(!strcmp(&value[j], "in") && j != 0)
                    {
                        value[j] = '\0';
                        int height = atoi(value);
                        if(height >= 59 && height <= 76) isValid[3] = 1;
                    }
                } else if(!strcmp(field, "hcl")) {
                    hasField[4] = 1;
                    if(value[0] == '#')
                    {
                        int colourLength = 1;
                        while((value[colourLength] >= '0' && value[colourLength] <= '9') || (value[colourLength] >= 'a' && value[colourLength] <= 'f')) colourLength++;
                        if(colourLength == 7) isValid[4] = 1;
                    }
                } else if(!strcmp(field, "ecl")) {
                    hasField[5] = 1;
                    if(!(strcmp(value, "amb") && strcmp(value, "blu") && strcmp(value, "brn") && strcmp(value, "gry") && strcmp(value, "grn") && strcmp(value, "hzl") && strcmp(value, "oth"))) isValid[5] = 1;
                } else if(!strcmp(field, "pid")) {
                    hasField[6] = 1;
                    int passportLength = 0;
                    while(value[passportLength] >= '0' && value[passportLength] <= '9') passportLength++;
                    if(passportLength == 9) isValid[6] = 1;
                }
            }
        }
        if(line[0] == '\n')
        {
            int numValidFields = 0;
            int numFields = 0;
            for(int i = 0; i < 7; i++) numValidFields += isValid[i];
            for(int i = 0; i < 7; i++) isValid[i] = 0;
            if(numValidFields == 7) numPassportsValid++;
            for(int i = 0; i < 7; i++) numFields += hasField[i];
            for(int i = 0; i < 7; i++) hasField[i] = 0;
            if(numFields == 7) numPassportsWithAllRequiredFields++;
        }
    }
    int numValidFields = 0;
    int numFields = 0;
    for(int i = 0; i < 7; i++) numValidFields += isValid[i];
    if(numValidFields == 7) numPassportsValid++;
    for(int i = 0; i < 7; i++) numFields += hasField[i];
    if(numFields == 7) numPassportsWithAllRequiredFields++;

    printf("%d passports had all 7 required fields.\n", numPassportsWithAllRequiredFields);
    printf("%d passports were valid.\n", numPassportsValid);
    return 0;
}
