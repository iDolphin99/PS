#include <stdio.h>
int count(int n, int i) {
	int cnt = 0;
	do {
		if (n % 10 == i) cnt++;
	} while (n /= 10);
	return cnt;
}
int main() {
	int i, in, tot=1;
	for (i = 0; i < 3; i++, tot *= in)
		scanf_s("%d", &in);
	for (i = 0; i < 10; i++)
		printf("%d \n", count(tot, i));

}