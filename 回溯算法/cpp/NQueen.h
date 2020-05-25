#pragma once
#include <vector>
#include <iostream>

using namespace std;

class Queen
{
	public:
		int x;
		int y;
		Queen(int xx = 0, int yy = 0) : x(xx), y(yy) {}
		void operator=(const Queen& q) { x = q.x; y = q.y; }
		bool operator==(const Queen& q)
		{
			if(x==q.x || y==q.y || (x+y)==(q.x+q.y) || (x-y)==(q.x-q.y))
				return true;
			else
				return false;
		}
};

bool is_valid(vector<Queen>& track, Queen& tmp_q)
{
	for (auto& x : track)
		if (x == tmp_q)
			return true;
	return false;

}

void backtrack(const int n, vector<Queen>& track, vector<vector<Queen> >& res)
{
	if (track.size() == n)
	{
		res.push_back(track);
		return;
	}

	for (int j=0; j<n; j++)
	{
		int i = track.size();
		Queen tmp_q = Queen(i, j);
		if(is_valid(track, tmp_q))
			continue;
		track.push_back(tmp_q);
		backtrack(n, track, res);
		track.pop_back();
	}
}


void use_backtrack(const int n)
{
	vector<vector<Queen> > res;
	vector<Queen> track;
	backtrack(n, track, res);
	for (auto& x : res)
	{	
		std::cout << "answer: \n";
		for (auto& q : x)
		{
			for (int i = 0; i < n; i++)
			{
				if (i == q.y)
					std::cout << "Q";
				else
					std::cout << "-";
			}
			std::cout << std::endl;
		}
		std::cout << std::endl;
	}
}