#include <stdio.h>
#include <stdlib.h>

int main()
{
	setvbuf(stdout, NULL, _IONBF, 0);
	
	printf("Long Long Candy(%%lld) + Long Long Candy = How many Candies?(%%d)\nI want -1 candies!\n\n");
	
	printf("How many candies?\n");
	signed long long int candy1;
	scanf("%lld", &candy1);
	
	printf("\nHow many more candies?\n");
	signed long long int candy2;
	scanf("%lld", &candy2);
	
	int totalCandy=0;
	totalCandy = candy1+candy2;
	
	if (candy1<0 || candy2<0)
	{
		printf("\nI can't count these candies.\n");
	}
	else if (totalCandy==-1)
	{
		printf("\nCandy + Candy = %d. Candy forever!\n", totalCandy);
		system("/bin/cat flag.txt");
	}
	else
	{
		printf("\nCandy + Candy = %d. Good things never last :(\n", totalCandy);
	}
}



