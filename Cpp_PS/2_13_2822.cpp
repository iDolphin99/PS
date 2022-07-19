#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;
bool compare(pair<int, int> a, pair<int, int> b) {
	if (a.second == b.second) return a.first < b.first;
	else return a.second < b.second;
}
int main() {
	int i, in, tot=0;
	vector<pair<int, int>> points;
	for (i = 0; i < 8; i++) {
		scanf_s("%d", &in);
		points.push_back(make_pair(in, i + 1));
	}
	sort(points.begin(), points.end());
	for (i = 0; i < 8; i++) {
		if (i < 3) points.erase(points.begin());
		else tot += points[i - 3].first;
	}
	sort(points.begin(), points.end(), compare);
	printf("%d\n", tot);
	for (i = 0; i < 5; i++) printf("%d ", points[i].second);
}