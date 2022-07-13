#include <stdio.h>
int main() {
	int n;
	scanf_s("%d", &n);
	for (int i = 1; i < 2*n; i++, printf("\n")) {
		if (i <= n) {
			for (int j = n; j > 0; j--)
				printf("%s", j > i ? " " : "*");
		}
		else {
			for (int j = 0; j < n; j++)
				printf("%s", j > i%n - 1 ? "*" : " ");
		}
	}
}