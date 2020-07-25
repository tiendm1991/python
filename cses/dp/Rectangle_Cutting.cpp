#include <iostream>
#include <bits/stdc++.h>

using namespace std;
#define ll long long
#define arr array<int, 2>
const int maxN = 500, maxInt = 1e9;
int dp[maxN + 1][maxN + 1];
int m, n;

int main() {
    cin >> m >> n;
    for (int i = 1; i <= m; i++){
        for(int j = 1; j <= n; j++){
            dp[i][j] = maxInt;
            if(i == j){
                dp[i][j] = 0;
                continue;
            }
            for (int k = 1; k < i; k ++){
                dp[i][j] = min(dp[i][j], dp[k][j] + dp[i-k][j] + 1);
            }
            for (int k = 1; k < j; k ++){
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[i][j-k] + 1);
            }
        }
    }
    cout << dp[m][n];
}
