#include <stdio.h>
#include <string.h>
void invitation() __attribute__((__section__(".special")));

void check() {
	char buff[20];
	scanf("%s", buff);
	printf("Heh, not so easy\n");
}

void invitation() {
	printf("\nOooo waittttt it seems you got it :)\n\n");
	printf("Pipe the command to \'nc pwn.chal.gryphonctf.com 18153\' to get the flaggg :)\n");
}

int main() {
	printf("Want the invitation? Gimme the secret code!\n");
	check();
}