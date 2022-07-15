#include <stdio.h>
int main() {
	int n, tot=0;
	scanf_s("%d", &n);
	for (int i = 1; i <= n; i++)
		tot += i * (n + 2);
	printf("%d", tot);
}