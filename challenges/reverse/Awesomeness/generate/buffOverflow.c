#include <stdio.h>
#include <string.h>
void win();

void check() {
	char buff[71];
	scanf("%s", buff);
	printf("Heh, you aren't awesome enuf! Not giving you the flag :)\n");
}

void admin() {
	printf("\nGCTF{Y0UR_4W3S0M3_BU7_N07_R34LLY}\n");
}

int main() {
	printf("ARE YOU AWESOME ENUF FOR THE FLAG?\n");
	printf("Let's find out!\n");
	printf("What's your name?\n");
	check();
}