#include <stdio.h>
int main() {
	int n; 
	scanf_s("%d", &n);
	for (int i = 1; i < 2 * n; i++, printf("\n")) {
		for (int j = 1; j < 2 * n + 1; j++) {
			if (i < n) printf("%s", i < j && j < 2 * n -i+1 ? " " : "*");
			else if (i == n) printf("*");
			else printf("%s", 2*n - i < j&& j < i+1 ? " " : "*");
		}
	}
}