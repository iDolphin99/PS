#include <stdio.h>
int main() {
	int n;
	scanf_s("%d", &n);
	for (int i = 1; i <= n; i++, printf("\n")) 
		for (int j = 0 ; j<2*n-i ; j++) 
			printf("%s", i-j-1 <= 0 ? "*" : " "); 
}