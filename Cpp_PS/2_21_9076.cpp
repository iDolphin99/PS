#include <stdio.h>
#include <algorithm>
int main() {
	int t, points[5];
	scanf_s("%d", &t);
	while (t--) {
		for (int i = 0; i < 5; i++) scanf_s("%d", &points[i]);
		std::sort(points, points + 5);
		points[3] - points[1] >= 4 ? printf("KIN\n") : printf("%d\n", points[1] + points[2] + points[3]);
	}
}