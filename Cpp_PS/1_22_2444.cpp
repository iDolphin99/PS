#include <stdio.h>
int main() {
	int n; 
	scanf_s("%d", &n);
	for (int i = 1; i < 2 * n; i++, printf("\n")) { 
		if (i <= n) {  
			for (int j = n + i - 1; j > 0; j--) 
				printf("%s", j > 2 * i - 1 ? " " : "*");
		}
		else
			for (int j = 0; j < 2 * n - i % n - 1; j++)   
				printf("%s", j > i%n -1 ? "*" : " ");
	}
}