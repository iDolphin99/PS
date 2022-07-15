#include <stdio.h>
int main() {
	int n; 
	scanf_s("%d", &n);
	for (int i = 0; i < n; i++, printf("\n")) {
		for (int j = 0; j < n + i; j++) {
			if (j > n - i - 2) {
				if (n%2 ==0) printf("%c", (i % 2 == 0 && j % 2 != 0) || (i % 2 != 0 && j % 2 == 0) ? '*' : ' ');
				else printf("%c", (i % 2 != 0 && j % 2 != 0) || (i % 2 == 0 && j % 2 == 0) ? '*' : ' ');
			}
			else printf(" ");}}	
}