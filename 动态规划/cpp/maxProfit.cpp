#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>

using namespace std;

int maxProfit_k_1(const vector<int>& prices)
{
    int dp_i_0 = 0;
    int dp_i_1 = -prices[0];
    for(int i=1; i<prices.size(); i++)
    {
        dp_i_0 = max({dp_i_1+prices[i], dp_i_0});
        dp_i_1 = max({-prices[i], dp_i_1});
    }
    return dp_i_0;
}

int maxProfit_k_2(const vector<int>& prices)
{
    int dp_i_1_0 = 0;
    int dp_i_1_1 = -prices[0];
    int dp_i_2_0 = 0;
    int dp_i_2_1 = -prices[0];
    for(int i=1; i<prices.size(); i++)
    {   
        dp_i_2_0 = max({dp_i_2_1+prices[i], dp_i_2_0});
        dp_i_2_1 = max({dp_i_1_0-prices[i], dp_i_2_1});

        dp_i_1_0 = max({dp_i_1_1+prices[i], dp_i_1_0});
        dp_i_1_1 = max({-prices[i], dp_i_1_1});
    }
    return dp_i_2_0;
}


int main()
{
    vector<int> prices = {3, 2, 6, 5, 0, 3};
    cout << maxProfit_k_2(prices) << endl;
    return 0;
}