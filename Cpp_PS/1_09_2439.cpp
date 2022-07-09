#include <stdio.h>
int main() {
	int n;
	scanf_s("%d", &n);
	for (int i = 1; i < n + 1; i++, printf("\n")) {
		for (int j = n; j > i; j--)
			printf(" ");
		for (int k = 0; k < i; k++)
			printf("*");
	}
	return 0;
}