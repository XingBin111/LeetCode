#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    void move_right(vector<int>& arr, int k){
        int n = arr.size() - 1;
        while(n >= k){
            arr[n] = arr[n-1];
            n--;
        }
    }
    void duplicateZeros(vector<int>& arr) {
        int n = arr.size();
        int i = 0;
        while(i<n){
            if(arr[i] == 0){
                move_right(arr, i);
                arr[i] = 0;
                i += 2;
            }
            else
                i++;
        }
    }
};

int main()
{
    vector<int> arr = {0,0,0,0,0,0,0};
    Solution s;
    s.duplicateZeros(arr);

    for(auto& x: arr)
        cout << x << endl;
    return 0;
}