#include <stdio.h>
int main() {
	int out, in, tot=0, max=0;
	for (int i = 0; i < 10; i++) {
		scanf_s("%d %d", &out, &in);
		max = (tot += in - out) > max ? tot : max; 
	}
	printf("%d", max);
}