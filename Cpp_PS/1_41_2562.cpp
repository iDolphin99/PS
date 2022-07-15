#include <stdio.h>
int main() {
	int in, max=0, num=0;
	for (int i = 0; i < 9; i++) {
		scanf_s("%d", &in);
		if (max < in) { 
			max = in; 
			num = i; }
	}
	printf("%d\n%d", max, num + 1);
}