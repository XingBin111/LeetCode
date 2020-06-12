#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <stdlib.h>


using namespace std;

int char2int(char c)
{
    int num;
    num = c - '0';  
    return num;
}

char int2char(int num)
{
    char c;
    c= num + '0';  
    return c;
}

string string_multiply(const string& s1, const string& s2)
{   
    int m = s1.size();
    int n = s2.size();
    string res(m+n, '0');
    for(int i=m-1; i>=0; i--)
    {
        for(int j=n-1; j>=0; j--)
        {
            int tmp = char2int(s1[i]) * char2int(s2[j]);
            tmp += char2int(res[i+j]) * 10 + char2int(res[i+j+1]);
            res[i+j+1] = int2char(tmp % 10);
            res[i+j] = int2char(tmp / 10);
        }
    }
    int i = 0;
    while(res[i] == '0')
        i++;

    return res.substr(i, res.size()-i);
}

void char2int_usage()
{
    string s1 = "123";
    for(char& x: s1)
        cout << char2int(x) << endl;
}

int main()
{
    string s1 = "123";
    string s2 = "445";
    string res = string_multiply(s1, s2);
    cout << res << endl;

    return 0;
}