#include <stdio.h>
int main() {
	int n, in, min = 1000000, max = -1000000;
	scanf_s("%d", &n);
	while (n--) {
		scanf_s("%d", &in);
		min = min > in ? in : min;
		max = max < in ? in : max;
	}
	printf("%d %d", min, max);
}