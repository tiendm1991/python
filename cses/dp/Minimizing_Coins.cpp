#include <iostream>
#include <bits/stdc++.h>

using namespace std;
#define ll long long
#define ar array
const int maxN = 100, maxS = 1e6;
int a[maxN];
ll dp[maxS+1];
int n, s;

int main()
{
    cin >> n >> s;
    for (int i = 0; i < n; i++)
        cin >> a[i];
    for (int i = 1; i <= s; i++){
        dp[i] = 1e9;
        for (int j = 0; j < n; j++){
            if (a[j] <= i ){
                dp[i] = min(dp[i], dp[i - a[j]] + 1);
            }
        }
    }
    if (dp[s] < 1e9){
        cout << dp[s];
    }else{
        cout << -1;
    }
}
