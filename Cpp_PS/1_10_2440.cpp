#include <stdio.h>
int main() {
	int n;
	scanf_s("%d", &n);
	for (int i = 0; i < n; i++, printf("\n"))
		for (int j = n; j > i; j--)
			printf("*");
	return 0;
}