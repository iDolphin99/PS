#include <stdio.h>
int main() {
	int t, n, c; 
	float g;
	scanf_s("%d", &t);
	for (int i = 0; i < t; i++) {
		int credit = 0; 
		float gpa = 0.0; 
		scanf_s("%d", &n);
		for (int j = 0; j < n; j++) {
			scanf_s("%d %f", &c, &g);
			credit += c; 
			gpa += g; 
		}
		printf("%d %f \n", credit, gpa/(float)n);
	}
	return 0; 
}

// {0, 0.7, 1, 1.3, 1.7, 2, 2.3, 2.7, 3, 3.3, 3.7, 4, 4.3