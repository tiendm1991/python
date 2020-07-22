#include <iostream>
#include <bits/stdc++.h>

using namespace std;
#define ll long long
#define ar array
const int maxN = 1e6;
int n, dp[maxN+1];

int main() {
    cin >> n;
    dp[0] = 0;
    for (int i = 1; i <= n; i++) {
        dp[i] = 1e9;
        int tmp = i;
        while (tmp > 0){
            int x = tmp % 10;
            if(x != 0){
                dp[i] = min(dp[i], dp[i - x] + 1);
            }
            tmp /= 10;
        }
    }
    cout << dp[n];
}
