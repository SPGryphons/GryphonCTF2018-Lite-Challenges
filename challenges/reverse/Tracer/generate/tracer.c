#include <stdio.h>
#include <stdint.h>
#include <string.h>

int main(int argc, char const *argv[])
{
    uint8_t length = 28;
    uint8_t array[29] = {61, 57, 74, 60, 113, 104, 41, 108, 41, 72, 43, 63, 68, 47, 85, 95, 43, 85, 57, 42, 100, 89, 41, 72, 38, 75, 112, 115, 0};
    for (int i = 0; i < length; i++) {
        array[i] += 10;
    }
    printf("Someone recover our flag!\n> ");
    uint8_t buf[length+1];
    fgets(buf,length+1,stdin);
    if (strcmp(buf, array) == 0) {
        printf("Thanks love, the flag's back\n");
    } else {
        printf("That's not my flag :(\n");
    }
    return 0;
}