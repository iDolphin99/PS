#include <stdio.h>
int main() {
	int n, tot=-1, min=99;
	for (int i =0; i<7; i++){
		scanf_s("%d", &n);
		if (n % 2 != 0) {
			tot += n;
			if (min > n) min = n;
		}
	}
	tot >= 0 ? printf("%d\n%d", tot + 1, min) : printf("%d", tot);
}