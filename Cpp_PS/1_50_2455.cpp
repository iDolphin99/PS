#include <stdio.h>
int main() {
	int on, off, tot=0, max=0;
	for (int i = 0; i < 4; i++) {
		scanf_s("%d %d", &off, &on);
		tot += on - off;
		max = tot > max ? tot : max;
	}
	printf("%d", max);
}