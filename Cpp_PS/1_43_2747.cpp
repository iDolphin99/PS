#include <stdio.h>
int fibo(int n) {
	int n0 = 0, n1 = 1, n2=1;
	if (n == 1) return n1; 
	else {
		for (int i = 2; i < n; i++) { 
			n0 = n1;
			n1 = n2; 
			n2 = n1 + n0;}
	}
	return n2;
}
int main() {
	int n;
	scanf_s("%d", &n);
	printf("%d", fibo(n));
}