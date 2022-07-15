#include <stdio.h>
int main() {
	int n, fac =1;
	scanf_s("%d", &n);
	for (int i = n; i > 0; i--)
		fac = fac * i;
	printf("%d", fac);
}