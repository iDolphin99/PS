#include <stdio.h>
#include <algorithm>
int main() {
	int t, arr[10];
	scanf_s("%d", &t);
	while (t--) {
		for (int i = 0; i < 10; i++) scanf_s("%d", &arr[i]);
		std::sort(arr, arr + 10);
		printf("%d\n", arr[7]);
	}
}