#include <stdio.h>
int main() {
	int mod[42] = {0}, in, cnt = 0;
	for (int i = 0; i < 10; i++) {
		scanf_s("%d", &in);
		++mod[in % 42] == 1 ? cnt++ : cnt = cnt;
	}
	printf("%d", cnt);
}