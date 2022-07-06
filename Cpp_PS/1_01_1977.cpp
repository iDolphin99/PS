// 1977. 완전제곱수 
#include <iostream>

using namespace std;

int main()
{
	int M, N, sum = 0, min = 0;

	cout << "";
	cin >> M >> N;

	for (int i = 0; i*i <= N; i++){
		if (i * i >= M && i * i <= N){
			sum += i * i;
			if (min == 0)
				min = i * i;
		}
	}

	if (sum != 0)
		cout << sum << "\n" << min;
	else
		cout << -1;

	return 0;
}