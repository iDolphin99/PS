#include <stdio.h>
#include <map>
using namespace std;
int main() {
	int in, tot=0;
	map<int, int> num;
	for (int i = 0; i < 8; i++) {
		scanf_s("%d", &in);
		num[in] = i + 1;
	}
	for (int i = 7; i > 2; i++) { printf("%d \t", num.at(i)); }
}