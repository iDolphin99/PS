#include <iostream>

int main() {
	int n = 0;

	std::cin >> n;

	for (int i = 0; i < n; i++)
		std::cout << i + 1 << '\n';

	return 0;
}