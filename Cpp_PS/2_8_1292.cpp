#include <stdio.h>
int main() {
	int a, b, tot = 0, ans = 0;
	scanf_s("%d %d", &a, &b);
	for (int i = 1; i < 46; i++, tot += i-1) 
		for (int j = 1; j <= i; j++)
			if (a<= j+tot && j + tot<= b) ans += i;
	printf("%d\n", ans);
}