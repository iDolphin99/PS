#include <stdio.h>
int main() {
	int n;
	scanf_s("%d", &n);
	for (int i = 1; i < 2 * n; i++, printf("\n")) {
		for (int j = 1; j < 2 * n; j++) {
			if (i < n && j <= 2*n-i)  printf("%s", i <= j ? "*" : " ");
			else if (i == n && j <=n) printf("%s", j==n ? "*" : " ");
			else if (i > n && j <= i) printf("%s", 2 * n - i <= j ? "*" : " ");
		}
	}
}