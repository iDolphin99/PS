// 11098, ÿ�ø� ������
// endl���ٴ� '\n'�� �ӵ��� �����Ѵٰ� �մϴ�.. ��..
#include <iostream>

using namespace std;

int main() {
	int n, p;

	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> p;
	
		int pay, max = 0;
		string name, max_name;

		for (int j = 0; j < p; j++) {
			cin >> pay >> name;
			if (pay >= max) { 
				max = pay;
				max_name = name;}
		}
		cout << max_name << '\n';
	}

	return 0;
}