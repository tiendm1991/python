#include <iostream>
#include <bits/stdc++.h>

using namespace std;
#define ll long long
#define arr array<int, 2>
const int maxN = 1e5, maxM = 100, mod = 1e9 + 7;
int x[maxN];
ll dp[maxN][maxM + 1];
int n, m;

int main() {
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        cin >> x[i];
    }
    if (x[0] == 0) {
        for (int i = 1; i <= m; i++) {
            dp[0][i] = 1;
        }
    } else {
        dp[0][x[0]] = 1;
    }

    for (int i = 1; i < n; i++) {
        int start = 1;
        int end = m;
        if (x[i] != 0) {
            start = x[i], end = x[i];
        }
        for (int j = start; j <= end; j++) {
            dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1] + dp[i - 1][j + 1]) % mod;
        }
    }
    ll ans = 0;
    for (int i = 1; i <= m; i++) {
        ans += dp[n - 1][i];
    }
    cout << ans%mod;
}
