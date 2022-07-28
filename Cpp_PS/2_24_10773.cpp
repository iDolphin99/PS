#include <stdio.h>
#include <vector>
using namespace std;
int main() {
	int k, in, tot=0;
	vector <int> vec;
	scanf_s("%d", &k);
	while (k--) {
		scanf_s("%d", &in);
		if (in == 0) {
			tot -= vec[vec.size()-1];
			vec.pop_back();}
		else {
			vec.push_back(in);
			tot += in;}
	}
	printf("%d", tot);
}