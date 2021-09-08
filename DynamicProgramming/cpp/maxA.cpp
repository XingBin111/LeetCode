#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>

using namespace std;

int maxA(int N)
{
    vector<int> dp_table(N+1, 0);
    for(int i=1; i<N+1; i++)
    {   
        dp_table[i] = dp_table[i-1]+1;
        for(int j=2; j<i; j++)
            dp_table[i] = max({dp_table[i], dp_table[j-2]*(i-j+1)});
    }
    return dp_table[N];
}

int main()
{
    int N = 11;
    cout << maxA(N) << endl;
    return 0;
}