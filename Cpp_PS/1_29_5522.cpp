#include <stdio.h>
int main() {
	int n, tot = 0;
	for (int i = 0; i < 5; i++) {
		scanf_s("%d", &n);
		tot += n;
	}
	printf("%d", tot);
}