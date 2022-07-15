#include <stdio.h>
#include <vector>
using namespace std;
int main() {
	int n, x, b;
	scanf_s("%d %d", &n, &x);
	vector <int> a;
	while (n--) {
		scanf_s("%d", &b);
		if (b < x) a.push_back(b);}
	for (auto e : a)
		printf("%d ", e);
}