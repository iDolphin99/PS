#include <stdio.h>
int main() 
{ 
	int n;
	scanf_s("%d", &n);
	for (int i = 0; i < n; i++, printf("\n")) {
		for (int j = n-i-1; j > 0; j--) printf(" ");
		for (int k = 0; k < 1 + (2 * i); k++) printf("*");
	}
}