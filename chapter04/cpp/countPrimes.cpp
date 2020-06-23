#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include "limits.h"

using namespace std;

int countPrimesI(int n)
{
    vector<int> nums(n, 1);
    int i = 2;
    while(i < n)
    {
        if(nums[i] == 1)
        {
            for(int j=2*i; j<n; j+=i)
                nums[j] = 0;
        }
        i++;
    }

    int res = 0;
    for(int j=2; j<n; j++)
        if(nums[j] == 1)
            res++;
    return res;
}  

int countPrimesII(int n)
{
    vector<int> nums(n, 1);
    int i = 2;
    while(i*i < n)
    {
        if(nums[i] == 1)
        {
            for(int j=i*i; j<n; j+=i)
                nums[j] = 0;
        }
        i++;
    }

    int res = 0;
    for(int j=2; j<n; j++)
        if(nums[j] == 1)
            res++;
    return res;
} 

int main()
{
    int n = 200;
    cout << countPrimesI(n) << endl;
    cout << countPrimesII(n) << endl;
    return 0;
}