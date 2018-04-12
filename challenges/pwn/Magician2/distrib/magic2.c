#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

void pwn();
void win();

const int sizeOfBuf = 256;
	
int main()
{
	//disable output buffering
	setvbuf(stdout, NULL, _IONBF, 0);
	
	//flavour print text
	puts("Prove to me magicians can read minds!");
	printf("Before you start, please tell me your name (%d chars max): \n", sizeOfBuf);
	
	pwn();	
}
void pwn()
{
	srand(time(NULL));
	int secretnum = (rand() % 1000000) + 1000000; 
	printf("(psst, this aint no magic trick, he's tricky!) %p\n",&secretnum);
	
	char buf[sizeOfBuf];
	
	//get input
	fgets(buf, sizeOfBuf, stdin);
	
	//concat str
	strcat(buf, "'s prediction: "); 
	
	//output text
	puts("I'm thinking of a random number (0 to 1000000), can you tell me what it is?");

	//print user's name + concat string
	printf(buf);
	
	//get "input"
	char num[8];
	fgets(num,8,stdin);
	
	if (secretnum==50)
	{
		win();
	}
	else 
	{
		printf("HA! the answer was %d see I knew you couldn't read my mind.\n", secretnum); 
	}
}
void win()
{
	//I WONDER WHAT IS THIS FUNCTION????
	puts("Magic??");
	system("/bin/cat flag.txt");
}
