#pragma once
#include <vector>

using namespace std;

template <typename T>
void backtrack(const vector<T>& nums, vector<T>& track, vector<vector<T> >& res)
{
	if (track.size() == nums.size())
	{
		res.push_back(track);
		return;
	}	
	
	for (auto& x : nums)
	{
		if (find(track.begin(), track.end(), x) != track.end())
			continue;
		track.push_back(x);
		backtrack(nums, track, res);
		track.pop_back();
	}
}

template <typename T>
void use_backtrack(const vector<T>& nums)
{
	vector<vector<int> > res;
	vector<int> track;
	backtrack(nums, track, res);
	for (auto& x : res)
	{
		for (auto& y : x)
			cout << y << "  ";
		cout << endl;
	}
}