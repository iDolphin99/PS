#include <stdio.h>
int main() {
	int n, in, tot=0, con=0;
	scanf_s("%d", &n);
	while (n--) {
		scanf_s("%d", &in);
		if (in == 1) {
			con++;
			tot += con * 1;
		}
		else con = 0;
	}
	printf("%d", tot);
}