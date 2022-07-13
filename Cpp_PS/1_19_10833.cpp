#include <stdio.h>
int main() {
	int n;
	int student, apple, tot=0;
	scanf_s("%d", &n);
	while (n--) {
		scanf_s("%d %d", &student, &apple);
		tot += (apple % student);
	}
	printf("%d", tot);
	return 0; 
}