/*
给定一个向量, 返回向量中元素连续的最大乘积, 
输入[2, 3, -2, 4], 返回6, 因为连续最大乘积为2*3
输入[-2,0,-1], 返回0

思路: 使用动态规划, 记录2个值:最大值imax, 和最小值imin

this is very similar to the " max cumulative sum subarray" problem. here you keep 2 values: the max cumulative product UP TO current 
element starting from SOMEWHERE in the past, and the minimum cumuliative product UP TO current element . 
it would be easier to see the DP structure if we store these 2 values for each index, like maxProduct[i],minProduct[i] .

at each new element, u could either add the new element to the existing product, or start fresh the product from current index (wipe out previous results), 
hence the 2 Math.max() lines.

if we see a negative number, the "candidate" for max should instead become the previous min product, 
because a bigger number multiplied by negative becomes smaller, hence the swap()
*/


#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;


int maxProduct_full_dp(const vector<int>& A){
    int n = A.size();
    vector<int> imax(n, A[0]);
    vector<int> imin(n, A[0]);
    int max_val = A[0];

    for(int i=1; i<n; i++){
        if(A[i] < 0)
            swap(imax[i-1], imin[i-1]);

        imax[i] = max(A[i], imax[i-1] * A[i]);
        imin[i] = min(A[i], imin[i-1] * A[i]);
        max_val = max(imax[i], max_val);
    }
    return max_val;
}

int maxProduct(const vector<int>& A) {
    int n = A.size();
    
    // store the result that is the max we have found so far
    int r = A[0];

    // imax/imin stores the max/min product of
    // subarray that ends with the current number A[i]
    for (int i = 1, imax = r, imin = r; i < n; i++) {
        // multiplied by a negative makes big number smaller, small number bigger
        // so we redefine the extremums by swapping them
        if (A[i] < 0)
            swap(imax, imin);

        // max/min product for the current number is either the current number itself
        // or the max/min by the previous number times the current one
        imax = max(A[i], imax * A[i]);
        imin = min(A[i], imin * A[i]);

        // the newly computed max value is a candidate for our global result
        r = max(r, imax);
    }
    return r;
}

int main(){
    vector<int> nums = {2, 3, -2, 4};
    cout << maxProduct(nums) << endl;
    cout << maxProduct_full_dp(nums) << endl;
    return 0;
}