#include <stdio.h>
#include <algorithm>
#include <vector>
using namespace std;
int main() {
	int n, in;
	float tot=0.0;
	vector <float> scores;
	scanf_s("%d", &n);
	while (~scanf_s("%d", &in))
		scores.push_back((float)in);
	sort(scores.begin(), scores.end());
	for (auto e : scores) 
		tot += e / scores.back() * 100.0;
	printf("%f", tot/n);
}