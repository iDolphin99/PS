#include <stdio.h>
#include <algorithm>
int main() {
	int n, num[50];
	scanf_s("%d", &n);
	for (int i = 0; i < n;i++)
		scanf_s("%d", &num[i]);
	std::sort(num, num + n);
	printf("%d", num[0] * num[n - 1]);
}