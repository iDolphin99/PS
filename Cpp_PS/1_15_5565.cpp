#include <stdio.h>
#include <vector>
#include <numeric>

using namespace std;

int main() {
	int tot, res; 
	vector<int>prices(9);

	scanf_s("%d", &res);
	for (int i = 0; i < prices.size() ; i++)
		scanf_s("%d", &prices[i]);
	tot = accumulate(prices.begin(), prices.end(), 0);

	printf("%d", res - tot);

	return 0; 
}