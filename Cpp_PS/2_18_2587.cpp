#include <stdio.h>
int main() {
	int i, in, tot = 0, num[10] = {0,};
	for (i = 0; i < 5; i++, tot+=in) {
		scanf_s("%d", &in);
		num[in / 10]++;
	}
	for (i = 0, in = 0; in < 3; i++) 
		if (num[i] != 0) in += num[i];
	printf("%d\n%d", tot / 5, (i-1)*10);
}