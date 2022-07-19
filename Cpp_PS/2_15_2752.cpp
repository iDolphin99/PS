#include <stdio.h>
#include <algorithm>
int main() {
	int i, n[3];
	for (i = 0; i < 3; i++)
		scanf_s("%d", &n[i]);
	std::sort(n, n + 3);
	for (i = 0; i < 3; i++)
		printf("%d ", n[i]);
}