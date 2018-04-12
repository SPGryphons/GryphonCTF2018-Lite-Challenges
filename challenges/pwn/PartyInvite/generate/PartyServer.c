#include <stdio.h>
#include <string.h>
void invitation() __attribute__((__section__(".special")));

void check() {
	char buff[20];
	scanf("%s", buff);
	printf("Heh, not so easy\n");
	fflush(stdout);
}

void invitation() {
	printf("Oooo waittttt it seems you got it :)\n\n");
	printf("%35s", "PARTY OF THE YEAR INVITATION\n");

	for (int i = 0; i < 40; i++) {
		putchar('=');
	}

	printf("\n%28s\n\n%38s\n%33s\n",
		"Congratulations",
		"Use this to gain access to the party",
		"GCTF{4W3S0M3_L177L3_P4R7Y}");

	for (int i = 0; i < 40; i++) {
		putchar('=');
	}

	putchar('\n');

	fflush(stdout);
}

int main() {
	printf("Want the invitation? Gimme the secret code!\n");
	fflush(stdout);
	check();
}