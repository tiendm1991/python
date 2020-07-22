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
        int choose = 0;
        while (tmp > 0){
            int x = tmp % 10;
            choose = max(choose, x);
            tmp /= 10;
        }
        dp[i] = min(dp[i], dp[i - choose] + 1);
    }
    cout << dp[n];
}
