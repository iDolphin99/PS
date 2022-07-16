#include <stdio.h>
int main() {
	int n, m, i, j;
	char spell[81];
	scanf_s("%d", &n);
	for (i = 0; i < n; i++) {
		scanf_s("%d %s", &m, &spell, sizeof(spell));
		for (j = m-1; j < sizeof(spell)-1; j++)
			spell[j] = spell[j + 1];
		spell[j] = '\0';
		printf("%s\n", spell);
	}
}