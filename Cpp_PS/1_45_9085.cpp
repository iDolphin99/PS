#include <stdio.h>
int main() {
	int t, n, in, sum=0;
	scanf_s("%d", &t);
	while (t--) {
		scanf_s("%d", &n);
		while (n--) {
			scanf_s("%d", &in);
			sum += in;
		}
		printf("%d\n", sum);
		sum = 0;
	}
}