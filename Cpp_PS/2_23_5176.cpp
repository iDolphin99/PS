#include <stdio.h>
int main() {
	int k, p, m, i, in, ans=0;
	scanf_s("%d", &k);
	while (k--) {
		scanf_s("%d %d", &p, &m);
		int arr[501] = {0};
		for (i = 0, ans=0; i < p; i++, arr[in]++) {
			scanf_s("%d", &in);
			if (arr[in] != 0) ans++;
		}
		printf("%d\n", ans);
	}
}