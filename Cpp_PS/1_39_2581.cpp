#include <stdio.h>
int main() {
	int m, n, cnt=0, tot=-1, min=0;
	scanf_s("%d\n%d", &m, &n);
	for (int i = n; i > m-1; i--, cnt=0) {
		for (int j = 1; j <= i; j++)
			if (i % j == 0) cnt++;
		if (cnt == 2) { tot += i; min = i; }
	}
	if (tot == -1) printf("%d", tot);
	else printf("%d\n%d",tot+1, min);
}