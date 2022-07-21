#include <stdio.h>
#include <algorithm>
int main() {
	int i, j, n1=0, n2=1, tot=0, height[9];
	for (i = 0; i < 9; i++, tot+= height[i-1]) scanf_s("%d", &height[i]);
	std::sort(height, height + 9);
	for (i = 8; i > 0; i--) {
		for (j = i - 1; j >= 0; j--) 
			if ((tot - height[i] - height[j]) == 100) { n1 = i; n2 = j; }}
	for (i = 0; i < 9; i++) 
		if (i != n1 && i != n2) printf("%d\n", height[i]);
}