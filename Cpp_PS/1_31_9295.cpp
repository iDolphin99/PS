#include <stdio.h>
int main() {
	int n, a, b; 
	scanf_s("%d", &n);
	for (int i =0; i<n; i++) {
		scanf_s("%d %d", &a, &b);
		printf("Case %d: %d \n", i+1, a+b);
	}
}