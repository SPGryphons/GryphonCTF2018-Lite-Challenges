#include <stdio.h>
#include <string.h>

void print(int * text, int i) {
	i = i / sizeof(int);
	i--;
	for (int j = 0; i >= 0; i--, j++) {
		int cs = text[i];
		cs -= j + 1;
		printf("%c", (char)cs);
	}
}

void check() {
	char buff[20];
	scanf("%s", buff);
	printf("Heh, you aren't awesome enuf! Not giving you the flag :)\n");
}

void admin() {
	int text[] = {37, -105, 76, 101, 71, 105, 72, 107, 71, 113, 99, 111, 100, 62, 102, 107, 94, 93, 60, 93, 78, -127, 75, 88, 70, 73, 11};
	print(text, sizeof(text));
}

int main() {
	printf("ARE YOU AWESOME ENUF FOR THE FLAG?\n");
	printf("Let's find out!\n");
	printf("What's your name?\n");
	check();
}