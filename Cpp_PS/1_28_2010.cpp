#include <stdio.h>
int main() {
	int n, plug, tot=1;
	scanf_s("%d", &n);
	while (n--) {
		tot -= 1; 
		scanf_s("%d", &plug);
		tot += plug;
	}
	printf("%d", tot);
}