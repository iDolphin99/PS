#include <stdio.h>
int main() {
	int t, n;
	scanf_s("%d", &t);
	for (int j = 0; j<t; j++, printf("\n")){
		scanf_s("%d", &n);
		for (int i = 0; n > 0; i++, n/=2) 
			if (n % 2 == 1) printf("%d ", i);
	}
}