#include <stdio.h>
#include <string.h>

int main() {
	char str[] = "\nGCTF{GU3SS_Y0U_R_4W3S0M3}\n", *msg;
	int output[strlen(str) + 1];

	for (int i = strlen(str) - 1, j = 0; i >= 0; i--, j++) {
		str[i] += i + 1;
		output[j] = (int)str[i];
		if (i != 0) {
			msg = "%d, ";
		} else {
			msg = "%d\n";
		}
		printf(msg, output[j]);
	}

	for (int i = strlen(str) - 1, j = 0; i >= 0; i--, j++) {
		int cs = output[i];
		cs -= j + 1;
		printf("%c", (char)cs);
	}
}