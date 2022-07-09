#include <stdio.h>
#include <numeric>
int GCD(int a, int b) {
	int n;
	while (b != 0) {
		n = a % b;
		a = b;
		b = n; 
	}
	return a;
}
int main() {
	int a, b, gcd, lcm, tmp;
	scanf_s("%d %d", &a, &b);

	if (b > a) {
		tmp = a; 
		a = b; 
		b = tmp; 
	}

	gcd = GCD(a, b); 
	if (!gcd)
		lcm = a * b;
	else
		lcm = (a * b) / gcd;

	printf("%d\n%d", gcd, lcm);
	return 0;
}