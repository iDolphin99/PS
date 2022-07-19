#include <stdio.h>
int main() {
	int i, in, min1=2000, min2=2000;
	for (i = 0; i < 3; i++) { scanf_s("%d", &in); min1 = min1 > in ? in : min1; }
	for (i = 0; i < 2; i++) { scanf_s("%d", &in); min2 = min2 > in ? in : min2; }
	printf("%d", min1 + min2 - 50);
}