#include <stdio.h>
#include <string.h>

void check() {
	char buff[20];
	scanf("%s", buff);
	printf("Heh, not so easy\n");
}

void awesome() {
	printf("\nOooo waittttt it seems you got it :)\nSend the secret code to the server at"
		" www.example.com:1000 to get an invitation!\n");
}

int main() {
	printf("I wonder what the secret code is hmmm...\n");
	check();
}