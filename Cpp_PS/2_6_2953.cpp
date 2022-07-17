#include <stdio.h>
int main() {
	int a, b, c, d, tot=0, max =0, ans=0;
	for (int i = 0; i < 5; i++, tot=0) {
		scanf_s("%d %d %d %d", &a, &b, &c, &d);
		tot = a + b + c + d;
		if (max < tot) { max = tot; ans = i; }
	}
	printf("%d %d", ans + 1, max);
}