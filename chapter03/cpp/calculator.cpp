#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <stdlib.h>
#include <stack>

using namespace std;

int calculate(const string& s)
{
    stack<int> st;
    int num = 0;
    char sign = '+';
    int res = 0;
    for(int i=0; i<s.size(); i++)
    {      
        int tmp;
        char c = s[i];
        if(isdigit(c))
            num = 10 * num + (c - '0');
        
        // 第二个条件是保证把最后一个整数入栈
        if(!isdigit(c) && c != ' ' || i == s.size() - 1)
        {
            switch (sign) {
                case '+':
                    st.push(num); break;
                case '-':
                    st.push(-num); break;
                case '*':
                    tmp = st.top() * num;
                    st.pop();
                    st.push(tmp);
                    break;
                case '/':
                    tmp = st.top() / num;
                    st.pop();
                    st.push(tmp);
                    break;
            }
            num = 0;
            sign = c;
        }
    }
    while (st.size() != 0)
    {
        res += st.top();
        st.pop();
    }
        
    return res;
}

int calculateII(vector<char> v)
{
    char sign = '+';
    int num = 0;
    int res = 0;
    stack<int> st;
    int tmp;
    while(v.size() > 0)
    {
        char c = *v.begin();
        v.erase(v.begin());

        if(isdigit(c))
            num = 10 * num + (c - '0');
        if(!isdigit(c) && c != ' ' || v.size()==0)
        {
            switch (sign) {
                case '+':
                    st.push(num); break;
                case '-':
                    st.push(-num); break;
                case '*':
                    tmp = st.top() * num;
                    st.pop();
                    st.push(tmp);
                    break;
                case '/':
                    tmp = st.top() / num;
                    st.pop();
                    st.push(tmp);
                    break;
            }
            num = 0;
            sign = c;
        }
    }
    while (st.size() != 0)
    {
        res += st.top();
        st.pop();
    }
    return res;
}

// vector可换成list
int calculate_parentheses(vector<char>& v)
{
    char sign = '+';
    int num = 0;
    int res = 0;
    stack<int> st;
    int tmp;
    while(v.size() > 0)
    {
        char c = *v.begin();
        v.erase(v.begin());

        if(isdigit(c))
            num = 10 * num + (c - '0');
        
        if(c == '(')
            num = calculate_parentheses(v);
        
        if((!isdigit(c) && c != ' ') || (v.size()==0 && c != ')'))
        {
            switch (sign) {
                case '+':
                    st.push(num); break;
                case '-':
                    st.push(-num); break;
                case '*':
                    tmp = st.top() * num;
                    st.pop();
                    st.push(tmp);
                    break;
                case '/':
                    tmp = st.top() / num;
                    st.pop();
                    st.push(tmp);
                    break;
            }
            num = 0;
            sign = c;
        }

        if(c == ')')
            break;
    }
    while (st.size() != 0)
    {
        res += st.top();
        st.pop();
    }
    return res;
}

void usage()
{
    string s = "-1-12*(3+1)";
    vector<char> v(s.size());
    for(int i=0; i<s.size(); i++)
        v[i] = s[i];
    cout << s << " = " << calculate_parentheses(v) << endl;
}

int main()
{
    usage();
    return 0;
}