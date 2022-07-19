#include <stdio.h>
#include <algorithm>
int main() {
	int in, n, num[1000];
	scanf_s("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf_s("%d", &in);
		num[i] = in;
	}
	std::sort(num, num + n);
	for (int i = 0; i < n; i++)
		printf("%d\n", num[i]);
}