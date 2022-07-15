#include <stdio.h>
int main() {
	int n, c, v; 
	scanf_s("%d", &n);
	while (n--) {
		scanf_s("%d %d", &c, &v);
		printf("You get %d piece(s) and your dad gets %d piece(s). \n", c / v, c % v);}
}