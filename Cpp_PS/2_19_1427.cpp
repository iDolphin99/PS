#include <stdio.h>
#include <algorithm>
int main() {
	int i, n, num[9];
	scanf_s("%d", &n);
	for (i = 0; n >0; i++, n /= 10)
		num[i] = n % 10;
	std::sort(num, num+i);
	for (i -=1; i >= 0; i--) printf("%d", num[i]);
}