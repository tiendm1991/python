
#include <iostream>
#include <bits/stdc++.h>

using namespace std;
#define ll long long
#define arr array<int, 2>
const int maxN = 1000, maxX = 1e5, mod = 1e9 + 7;
int h[maxN], s[maxN];
int dp[maxN + 1][maxX + 1];
int n, x;

int main() {
    cin >> n >> x;
    for (int i = 0; i < n; i++) {
        cin >> h[i];
    }
    for (int i = 0; i < n; i++) {
        cin >> s[i];
    }
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= x; j++) {
            if (j < h[i - 1]) {
                dp[i][j] = dp[i - 1][j];
            } else {
                dp[i][j] = max(dp[i - 1][j], s[i - 1] + dp[i - 1][j - h[i - 1]]);
            }
        }
    }

    cout << dp[n][x];
}
