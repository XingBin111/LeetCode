#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>

using namespace std;

// 时间效率为O(K*N^2),空间效率为O(KN)
int superEggDrop(int k, int N)
{
    if(k == 1)
        return N;
    if(N == 0)
        return 0;
    int res = INT32_MAX;
    for(int i=1; i<N+1; i++)
    {
        int broken_egg = superEggDrop(k-1, i-1);
        int not_broken = superEggDrop(k, N-i);
        int tmp = max({broken_egg, not_broken}) + 1;
        if(res > tmp)
            res = tmp;
    }
    return res;
}

int superEggDropBinSearch(int k, int N)
{
    if(k == 1)
        return N;
    if(N == 0)
        return 0;
    int res = INT32_MAX;
    int left = 1;
    int right = N + 1;
    while(left < right)
    {
        int mid = left + (right - left) / 2;
        int broken_egg = superEggDropBinSearch(k-1, mid-1);
        int not_broken = superEggDropBinSearch(k, N-mid);

        if (broken_egg < not_broken)
        {
            left = mid + 1;
            res = min({res, not_broken + 1});
        }
        else if (broken_egg > not_broken)
        {
            right = mid;
            res = min({res, broken_egg + 1});
        }
        else if (broken_egg == not_broken)
        {
            return broken_egg + 1;
        }
        
    }
    return res;
}

int main()
{   
    int k = 2;
    cout << superEggDropBinSearch(k, 10) << endl;
    return 0;
}