#include <iostream>

using namespace std;

int main(void)
{
	int N, min = 0, max = 0;

	cin >> N; 

	int* year = new int[N];
	int* month = new int[N];
	int* day = new int[N];
	string* name = new string[N];

	for (int i = 0; i < N; i++) {
		cin >> name[i] >> day[i] >> month[i] >> year[i];
		
		if (year[i] <= year[max])
		{
			if (year[i] < year[max]) max = i; 
			else
			{
				if (month[i] <= month[max])
				{
					if (month[i] < month[max]) max = i;
					else {
						if (day[i] < day[max]) max = i;
					}
				}
			}
		}
		
		if (year[i] >= year[min])
		{
			if (year[i] > year[min]) min = i;
			else
			{
				if (month[i] >= month[min])
				{
					if (month[i] > month[min]) min = i;
					else {
						if (day[i] > day[min]) min = i;
					}
				}
			}
		}
	}

	cout << name[min] << "\n" << name[max];
	
	return 0;
}

