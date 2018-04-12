#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>


char buf[11];

int main(int argc, char **argv) {
    
    puts("Prove to me magicians can read minds!");
    puts("Before you start, please tell me your name (10 chars max): ");
    fflush(stdout);
    fgets(buf, 11, stdin);
        
    strcat(buf, "'s prediction: ");  
    puts("I'm thinking of a random number (0 to 1000000), can you tell me what it is?");
    
    srand(time(NULL));
    int secretnum = rand() % 1000000;

    printf(buf);
    fflush(stdout);
    int prediction;
    char num[8];
    fgets(num,8,stdin);
    sscanf(num,"%d",&prediction);

    if (prediction == secretnum){
        printf("Unbelievable! Here's the flag: GCTF{f0rma7_57rIN9s_l3aK5_y0Ur_M3M0Ry}\n");
    } else {
        printf("HA! the answer was %d see I knew you couldn't read my mind.\n", secretnum); 
    }
    fflush(stdout);
    return 0;
}