#include <stdio.h>
long long fibonacci(int n) {
	long long n0 = 0, n1 = 1, n2=1;
	if (n == 0) return n0;
	else if (n == 1)
		return n1; 
	else {
		for (int i = 2; i <= n; i++) {
			n2 = n0 + n1; 
			n0 = n1; 
			n1 = n2; 
		}
		return n2;
	}
}
int main() {
	int n;
	scanf_s("%d", &n);
	printf("%llu", fibonacci(n));
	return 0; 
} 