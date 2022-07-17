#include <stdio.h>
int main() {
	int t, store, pos, min, max, i, j;
	scanf_s("%d", &t);
	for (j=0; j<t; j++, printf("%d\n", (max - min) * 2)) {
		scanf_s("%d", &store);
		for (i=0, min=99, max=0; i<store;i++) {
			scanf_s("%d", &pos);
			min = min > pos ? pos : min;
			max = max < pos ? pos : max; 
		}
	}
}