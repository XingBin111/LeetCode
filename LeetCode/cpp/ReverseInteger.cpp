#include <iostream>
#include <vector>
#include <stack>
#include <queue>

using namespace std;

class Solution {
public:
    int reverse(int x) {
        int a = INT_MAX / 10;
        int b = INT_MIN / 10;
        int res = 0;
        while(x)
        {
            if(res < b || res > a)
                return 0;
            res = res * 10 + (x % 10);
            x /= 10;
        }
        return res;

    }
};