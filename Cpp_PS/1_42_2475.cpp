#include <stdio.h>
int main() {
	int in, tot=0;
	for (int i = 0; i < 5; i++) {
		scanf_s("%d", &in);
		tot += in * in;
	}
	printf("%d", tot % 10);
}