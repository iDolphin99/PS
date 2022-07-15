#include <stdio.h>
int main() {
	unsigned int test, s, n, q, p;
	scanf_s("%d", &test);
	while (test--) {
		scanf_s("%d", &s);
		scanf_s("%d", &n);
		while (n--) {
			scanf_s("%d %d", &q, &p);
			s += p * q;}
		printf("%d \n", s);
	}
}