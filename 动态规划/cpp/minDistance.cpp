#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>

using namespace std;

struct double_string
{
    string s1;
    string s2;
    // double_string(const string&_s1, const string&_s2) {s1=_s1; s2=_s2;}
    double_string(const string _s1, const string _s2) {s1=_s1; s2=_s2;}
    bool operator==(const double_string& ds) const {return (s1==ds.s1 && s2==ds.s2);}
    friend ostream& operator<<(ostream& os, const double_string& ds) 
    {
        os << "string 1: " << ds.s1 << ", string 2: " << ds.s2; 
        return os;
    } 
};

namespace std
{
    template<>
    struct hash<double_string>
    {
        size_t operator() (const double_string& s) const noexcept
        {
            return  hash<decltype(s.s1)>()(s.s1) +
                    hash<decltype(s.s2)>()(s.s2);
        }
    }; // 间接调用原生Hash.
}

int minDistance(const string& s1, const string& s2)
{
    if(s1.size() == 0)   
        return s2.size();
    if(s2.size() == 0)   
        return s1.size();
    if(s1[0] != s2[0])
    {
        int insert = minDistance(s1, s2.substr(1, s2.size()-1));
        int _delete = minDistance(s1.substr(1, s1.size()-1), s2);
        int relpacement = minDistance(s1.substr(1, s1.size()-1), s2.substr(1, s2.size()-1));
        int min_distance = min({insert, _delete, relpacement}) + 1;
        return min_distance;
    }
    else
        return minDistance(s1.substr(1, s1.size()-1), s2.substr(1, s2.size()-1));
}

int minDistanceMemo(const string& s1, const string& s2, unordered_map<double_string, int>& memo)
{
    if(s1.size() == 0)   
        return s2.size();
    if(s2.size() == 0)   
        return s1.size();
    int min_distance;
    if(s1[0] != s2[0])
    {
        int insert = minDistanceMemo(s1, s2.substr(1, s2.size()-1), memo);
        int _delete = minDistanceMemo(s1.substr(1, s1.size()-1), s2, memo);
        int relpacement = minDistanceMemo(s1.substr(1, s1.size()-1), s2.substr(1, s2.size()-1), memo);
        min_distance = min({insert, _delete, relpacement}) + 1;
    }
    else
        min_distance = minDistanceMemo(s1.substr(1, s1.size()-1), s2.substr(1, s2.size()-1), memo);
    double_string tmp(s1, s2);
    memo[tmp] = min_distance;
    return min_distance; 
}

int minDistanceIteration(const string& s1, const string& s2)
{
    vector<vector<int> > dp_table(s1.size()+1, vector<int>(s2.size()+1, 0));
    for(int i=0; i<s1.size()+1; i++)
        dp_table[i][0] = i;

    for(int i=0; i<s2.size()+1; i++)
        dp_table[0][i] = i;
    
    for(int i=1; i<s1.size()+1; i++)
    {
        for(int j=1; j<s2.size()+1; j++)
        {
            if(s1[i-1] == s2[j-1])
            {
                dp_table[i][j] = dp_table[i-1][j-1];
            }
            else
            {
                dp_table[i][j] = min({dp_table[i-1][j], dp_table[i][j-1], dp_table[i-1][j-1]}) + 1;
            }
        }
    }
    return dp_table[s1.size()][s2.size()];
    
}

void show_unordered_map(const unordered_map<double_string, int>& memo)
{
    /*打印元素*/
	cout<<"memo中的元素如下："<<endl;
	for(unordered_map<double_string, int>::const_iterator it = memo.begin(); it != memo.end(); it++)
	{
		cout<<it->first<<" -> "<<it->second<<endl;
	}
}

int main()
{
    string s1 = "horse";
    string s2 = "ros";
    unordered_map<double_string, int> memo;
    // cout << minDistanceMemo(s1, s2, memo) << endl;
    // show_unordered_map(memo);
    cout << minDistanceIteration(s1, s2) << endl;
    return 0;
}