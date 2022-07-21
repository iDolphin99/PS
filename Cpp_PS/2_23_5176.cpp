#include <stdio.h>
int main() {
	int k, p, m, i, in;
	scanf_s("%d", &k);
	while (k--) {
		scanf_s("%d %d", &p, &m);
		int arr[500] = {0};
		for (i = 0; i < p; i++, arr[in]++)
			scanf_s("%d", &in);
		for (i = 1, in = 0; i <= m; i++)
			if (arr[i] != 1 && arr[i] != 0) in += (arr[i]-1); 
		printf("%d\n", in);
	}
}