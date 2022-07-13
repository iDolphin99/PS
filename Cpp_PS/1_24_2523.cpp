#include <stdio.h>
#define abs(x) (x > 0 ? x : -1*(x))
int main() {
	int n;
	scanf_s("%d", &n);
	for (int i = 1; i < 2 * n; i++, printf("\n")) {
		for (int j = 0; j <  n-abs(n-i); j++) 
			printf("*");
	}
}