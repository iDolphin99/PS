#include <stdio.h>
#include <math.h>
int main() {
	int n, in;
	scanf_s("%d", &n);
	int cnt = n;
	for(int i =0; i<n; i++) {
		scanf_s("%d", &in);
		for (int j = 2; j <= sqrt(in); j++)
			if (in % j == 0) {cnt--;  break;}
		if (in == 1) cnt--;
	}
	printf("%d", cnt);
}