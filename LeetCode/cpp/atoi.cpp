#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <limits.h>

using namespace std;

class Solution {
public:
    int myAtoi(string str) {
        int res = 0;
        int i = 0;
        int n = str.size();
        int pos = 1;
        
        while(i < n && str[i] == ' ')
            i++;
        
        if(i< n && (str[i] == '+' || str[i] == '-'))
            pos = (str[i++] == '-') ? -1 : 1;
        
        while(i < n && ('0' <= str[i] && str[i] <= '9')){
            if(res > INT_MAX / 10 || (res == INT_MAX / 10 && str[i] - '0' > INT_MAX % 10))
                return pos > 0 ? INT_MAX : INT_MIN;
            
            res = res * 10  + (str[i++] - '0');
            
        }
        return res * pos;
    }
};

int main(){
    string s = "-42";
    Solution S;
    cout << S.myAtoi(s) << endl;
    return 0;
}