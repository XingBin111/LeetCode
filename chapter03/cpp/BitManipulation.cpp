#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <stdlib.h>
#include <list>

using namespace std;

void bit_usage()
{   
    // 没什么卵用, 只能装逼, 唯一一个好用的是 n & (n-1)
    cout << "usage of bit: |\n";
    cout << ('a' | ' ') << endl;
    cout << ('A' | ' ') << endl;

    cout << "usage of bit: &\n";
    cout << ('b' & '_') << endl;
    cout << ('B' & '_') << endl;

    cout << "usage of bit: ^\n";
    cout << ('d' ^ ' ') << endl;
    cout << ('D' ^ ' ') << endl;

    cout << "判断x y是否异号:\n";
    int x = -1, y = 2;
    cout << ((x ^ y) < 0) << endl;

    x = 3, y = 2;
    cout << ((x ^ y) < 0) << endl;

    cout << "交换a b:\n";
    int a = 3, b = 2;
    a ^= b;
    b ^= a;
    a ^= b;
    cout << "a = " << a << ", b = " << b << endl;
    
    a = a ^ b;
    cout << a << endl;
}

// 利用n & (n - 1) 可以消除最后一个 1, 来求正整数n的二进制表中有几个1
int hammingWeight(int n)
{
    int res = 0;
    while(n > 0)
    {
        n = n & (n - 1);
        res++;
    }
    return res;
}

// 利用n & (n - 1) 可以消除最后一个 1, 来判断整数n是否为2的指数
bool isPowerOfTwo(int n)
{
    if(n<0) 
        return false;
    return n&(n-1) == 0;
}

int main()
{
    // bit_usage();

    cout << hammingWeight(5) << endl;
    return 0;
}