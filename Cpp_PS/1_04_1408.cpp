#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

int main() {
	string now, start, token, result;
	vector<int> n_vec, s_vec;
	int n_time, s_time, time; 

	getline(cin, now);
	getline(cin, start);

	stringstream ss1(now);
	stringstream ss2(start);
	
	n_vec.clear();
	s_vec.clear();

	while (getline(ss1, token, ':'))
		n_vec.push_back(stoi(token));
	while (getline(ss2, token, ':'))
		s_vec.push_back(stoi(token));

	n_time = 3600 * n_vec[0] + 60 * n_vec[1] + n_vec[2];
	s_time = 3600 * s_vec[0] + 60 * s_vec[1] + s_vec[2];
	

	if (s_time > n_time)
		time = s_time - n_time;
	else
		time = 86400 - (n_time - s_time);


	for (int i = 0, j = 3600; i < 3; i++, j/=60) { //3600 60 1 
		if (time/j >= 10) result += to_string(time/j) + ":";
		else result += "0" + to_string(time/j) + ":";
		time %= j;
	}

	cout << result.substr(0, 8);

	return 0;
}

/*
	time[0] = s_vec[0] - n_vec[0];

	if (s_vec[1] >= n_vec[1]) time[1] = s_vec[1] - n_vec[1];
	else {
		time[0] -= 1;
		time[1] = s_vec[1] + (60 - n_vec[1]);
	}

	if (s_vec[2] >= n_vec[2]) time[2] = s_vec[2] - n_vec[2];
	else {
		time[1] -= 1;
		time[2] = s_vec[2] + (60 - n_vec[2]);
	}

	if (n_vec[0] >= s_vec[0])
	{
		time[0] = 24 + time[0];
		//time[1] = 60 - time[1];
		//time[2] = 60 - time[2];
	}

	for (int i = 0; i < 3; i++) {
		if (time[i] >= 10) result += to_string(time[i]) + ":";
		else result += "0" + to_string(time[i]) + ":";
	}

*/