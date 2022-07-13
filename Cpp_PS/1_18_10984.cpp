#include <stdio.h>
using namespace std;
int main() {
	int t, n, c; 
	float g;
	scanf_s("%d", &t);
	for (int i = 0; i < t; i++) {
		int credit = 0; 
		float tot = 0.0; 
		scanf_s("%d", &n);
		for (int j = 0; j < n; j++) {
			scanf_s("%d %f", &c, &g);
			credit += c; 
			tot += g*c; 
		}
		printf("%d %.1f \n", credit, tot/credit);
	}
	return 0; 
}