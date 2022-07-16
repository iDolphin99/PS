#include <stdio.h>
#include <math.h>
int main() {
	int	a, b, aReverse=0, bReverse=0;
	scanf_s("%d %d", &a, &b);
	for (int i = 2; i >= 0; i--, a /= 10, b /= 10) {
		aReverse += a % 10 * pow(10, i);
		bReverse += b % 10 * pow(10, i);
	}
	printf("%d", aReverse > bReverse ? aReverse : bReverse);
}