#include <stdio.h>
#include <vector>
using namespace std;
int main() {
	int n, v, ans=0;
	vector <int> num;
	scanf_s("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf_s("%d", &v);
		num.push_back(v);
	}
	scanf_s("%d", &v);
	for (auto e : num) if (e == v) ans++;
	printf("%d", ans);
}