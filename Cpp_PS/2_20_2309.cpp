#include <stdio.h>
#include <algorithm>
int main() {
	int i, height[9];
	for (i = 0; i < 9; i++) scanf_s("%d", &height[i]);
	std::sort(height, height + 9);
	for (i = 0; i < 7; i++) {

		printf("%d\n", height[i]);
	}
	
}