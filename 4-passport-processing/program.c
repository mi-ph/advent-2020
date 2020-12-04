#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_LINE 4096

int main(void)
{
    char line[MAX_LINE];

    char param[4];
    char value[MAX_LINE];

    int validPassports = 0;
    int allFieldPassports = 0;
    int field[7] = {0, 0, 0, 0, 0, 0, 0};
    int valid[7] = {0, 0, 0, 0, 0, 0, 0};

    while(fgets(line, MAX_LINE, stdin))
    {
        for(int i = 0; line[i] != '\0'; i++)
        {
            if(line[i] == ':')
            {
                param[0] = line[i-3];
                param[1] = line[i-2];
                param[2] = line[i-1];
                param[3] = '\0';
                int j = 1;
                while(line[i+j] != ' ' && line[i+j] != '\n')
                {
                    value[j-1] = line[i+j];
                    j++;
                }
                value[j-1] = '\0';
                if(!strcmp(param, "byr"))
                {
                    field[0] = 1;
                    int numDigits = 0;
                    j = 0;
                    while(value[j] != '\0')
                    {
                        if(value[j] >= '0' && value[j] <= '9')
                        {
                            numDigits++;
                        } else {
                            numDigits = -12345;
                        }
                        j++;
                    }
                    if(numDigits == 4) {
                        int birthYear = atoi(value);
                        if(birthYear >= 1920 && birthYear <= 2002)
                        {
                            valid[0] = 1;
                        }
                    }
                } else if(!strcmp(param, "iyr")) {
                    field[1] = 1;
                    int numDigits = 0;
                    j = 0;
                    while(value[j] != '\0')
                    {
                        if(value[j] >= '0' && value[j] <= '9')
                        {
                            numDigits++;
                        } else {
                            numDigits = -12345;
                        }
                        j++;
                    }
                    if(numDigits == 4) {
                        int issueYear = atoi(value);
                        if(issueYear >= 2010 && issueYear <= 2020)
                        {
                            valid[1] = 1;
                        }
                    }
                } else if(!strcmp(param, "eyr")) {
                    field[2] = 1;
                    int numDigits = 0;
                    j = 0;
                    while(value[j] != '\0')
                    {
                        if(value[j] >= '0' && value[j] <= '9')
                        {
                            numDigits++;
                        } else {
                            numDigits = -12345;
                        }
                        j++;
                    }
                    if(numDigits == 4) {
                        int expirationYear = atoi(value);
                        if(expirationYear >= 2020 && expirationYear <= 2030)
                        {
                            valid[2] = 1;
                        }
                    }
                } else if(!strcmp(param, "hgt")) {
                    field[3] = 1;
                    j = 0;
                    while(value[j] != '\0' && value[j] >= '0' && value[j] <= '9')
                    {
                        j++;
                    }
                    if(!strcmp(&value[j], "cm") && j != 0)
                    {
                        value[j] = '\0';
                        int height = atoi(value);
                        if(height >= 150 && height <= 193) valid[3] = 1;
                    }
                    if(!strcmp(&value[j], "in") && j != 0)
                    {
                        value[j] = '\0';
                        int height = atoi(value);
                        if(height >= 59 && height <= 76) valid[3] = 1;
                    }
                } else if(!strcmp(param, "hcl")) {
                    field[4] = 1;
                    if(value[0] == '#')
                    {
                        int colourLength = 1;
                        while((value[colourLength] >= '0' && value[colourLength] <= '9') || (value[colourLength] >= 'a' && value[colourLength] <= 'f')) colourLength++;
                        if(colourLength == 7)
                        {
                            valid[4] = 1;
                        }
                    }
                } else if(!strcmp(param, "ecl")) {
                    field[5] = 1;
                    if(!(strcmp(value, "amb") && strcmp(value, "blu") && strcmp(value, "brn") && strcmp(value, "gry") && strcmp(value, "grn") && strcmp(value, "hzl") && strcmp(value, "oth")))
                    {
                        valid[5] = 1;
                    }
                } else if(!strcmp(param, "pid")) {
                    field[6] = 1;
                    int passportLength = 0;
                    while(value[passportLength] >= '0' && value[passportLength] <= '9') passportLength++;
                    if(passportLength == 9) {
                        valid[6] = 1;
                    }
                }
            }
        }
        if(line[0] == '\n')
        {
            int validFields = 0;
            int presentFields = 0;
            for(int i = 0; i < 7; i++) validFields += valid[i];
            for(int i = 0; i < 7; i++) valid[i] = 0;
            if(validFields == 7) validPassports++;
            for(int i = 0; i < 7; i++) presentFields += field[i];
            for(int i = 0; i < 7; i++) field[i] = 0;
            if(presentFields == 7) allFieldPassports++;
        }
    }
    int validFields = 0;
    int presentFields = 0;
    for(int i = 0; i < 7; i++) validFields += valid[i];
    for(int i = 0; i < 7; i++) valid[i] = 0;
    if(validFields == 7) validPassports++;
    for(int i = 0; i < 7; i++) presentFields += field[i];
    for(int i = 0; i < 7; i++) field[i] = 0;
    if(presentFields == 7) allFieldPassports++;

    printf("%d passports had all 7 required fields.\n", allFieldPassports);
    printf("%d passports were valid.\n", validPassports);
    return 0;
}
