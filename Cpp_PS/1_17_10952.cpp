#include <stdio.h>
int main() {
	int a, b; 
	while (true) {
		scanf_s("%d %d", &a, &b);
		if (a == 0) break;
		printf("%d \n", a + b);
	}
	return 0; 
}