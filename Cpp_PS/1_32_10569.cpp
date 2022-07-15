#include <stdio.h>
int main() {
	int t, v, e;
	scanf_s("%d", &t);
	while (t--) {
		scanf_s("%d %d", &v, &e);
		printf("%d\n", 2-v+e);
	}
}