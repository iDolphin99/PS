#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
	int in, tot=0, mode = 0, count =1, countMode =1;
	vector <int> num;
	for (int i = 0; i < 10; i++, tot+=in) { 
		scanf_s("%d", &in); 
		num.push_back(in); 
	}
	sort(num.begin(), num.end());
	for (int j = 1; j < 10; j++) {
		count = num[j] == num[j - 1] ? ++count : 1;
		if (countMode <= count) {
			mode = num[j];
			countMode = count;
		}
	}
	printf("%d\n%d", tot / 10, mode);
}