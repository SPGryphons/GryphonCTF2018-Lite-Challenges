#include <stdio.h>
#include <stdlib.h>

int main()
{
	setvbuf(stdout, NULL, _IONBF, 0);
	
	printf("Candy + Candy?\n\n");
	
	printf("How many candies?\n");
	int number1=0;
	scanf("%d", &number1); //non-integer values not read to stdin, shouldn't be a problem?
	
	printf("\nHow many more candies?\n");
	int number2=0;
	scanf("%d", &number2);
	
	if (number1<0 || number2<0)
	{
		printf("\nI can't count these candies.\n");
	}
	else if (number1+number2<0)
	{
		printf("\nCandy + Candy = %d. Candy forever!\n", number1+number2);
		system("/bin/cat flag.txt");
	}
	else
	{
		printf("\nCandy + Candy = %d. Good things never last :(\n", number1+number2);
	}
}



