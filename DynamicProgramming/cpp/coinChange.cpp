#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

int coin_change(const vector<int>& coins, int amount)
{
    
    if(amount == 0)
        return 0;
    int res = amount;
    int tmp = amount;
    for(vector<int>::const_iterator iter=coins.begin(); iter!=coins.end(); iter++)
    {   
        if(amount < *iter)
            continue;
        tmp = coin_change(coins, amount-*iter) + 1;
        if(tmp < res)
            res = tmp;
    }
    return res;
}

int coin_change_memo(const vector<int>& coins, int amount, unordered_map<int, int>& coin_map)
{
    if(amount == 0)
        return 0;
    if(coin_map.count(amount))
        return coin_map[amount];
    int res = amount;
    int tmp = amount;
    for(vector<int>::const_iterator iter=coins.begin(); iter!=coins.end(); iter++)
    {   
        if(amount < *iter)
            continue;
        tmp = coin_change_memo(coins, amount-*iter, coin_map) + 1;
        if(tmp < res)
            res = tmp;
    }
    coin_map[amount] = res;
    return res;
}

void show_unordered_map(const unordered_map<int, int>& coin_map)
{
    /*打印元素*/
	cout<<"coin_map中的元素如下："<<endl;
	for(unordered_map<int, int>::const_iterator it = coin_map.begin(); it != coin_map.end(); it++)
	{
		cout<<it->first<<"->"<<it->second<<endl;
	}
}


// 时间复杂度O(kn), 空间复杂度O(n)
int coin_change_iteration(const vector<int>& coins, int amount)
{
    vector<int> amount_vec(amount+1, 1);
    for(int i=1; i<amount+1; i++)
    {   
        int res = i;
        int tmp = res;
        for(vector<int>::const_iterator coint_it=coins.begin(); coint_it!=coins.end(); coint_it++)
        {
            if(i< *coint_it)
                continue;
            tmp  = amount_vec[i-*coint_it] + 1;
            if(tmp < res)
                res = tmp;
        }
        amount_vec[i] = res;
    }
    return amount_vec[amount];
}

int main()
{
    vector<int> coins = {1, 2, 5};
    int amount = 16;
    // unordered_map<int, int> coin_map;
    // cout << coin_change_memo(coins, amount, coin_map) << endl;
    // show_unordered_map(coin_map);
    cout << coin_change_iteration(coins, amount) << endl;
    return 0;
}