#include <stdio.h>
int main() {
	int day, in, cnt=0;
	scanf_s("%d", &day);
	for (int i = 0; i < 5; i++){
		scanf_s("%d", &in);
		if (in == day) cnt++;
	}
	printf("%d", cnt);
}