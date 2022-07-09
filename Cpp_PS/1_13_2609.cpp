#include <stdio.h>
#include <numeric>
int main() {
	int a, b; 
	scanf_s("%d %d", &a, &b);
	printf("%d\n%d", std::gcd(a, b), (a, b));
	return 0;
}