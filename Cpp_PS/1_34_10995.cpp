#include <stdio.h>
int main() {
	int n;
	scanf_s("%d", &n);
	for (int i = 0; i < n; i++, printf("\n")) {
		for (int j = 0; j < 2*n; j++) {
			if (i%2==0 && j < 2*n-1) printf("%s", j % 2 == 0 ? "*" : " ");  
			if (i%2!=0) printf("%s", j % 2 != 0 ? "*" : " "); 
		}
	}
}