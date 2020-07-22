#include <iostream>
#include <bits/stdc++.h>

using namespace std;
#define ll long long
#define ar array
const int maxN = 1000, mod = 1e9+7;
string s[maxN];
ll dp[maxN + 1][maxN + 1];
int n;

int main() {
    cin >> n;
    for (int i = 0; i < n; i++){
        cin >> s[i];
        dp[0][i+1] = 0;
        dp[i+1][0] = 0;
    }

    if (s[0][0] == '*' || s[n-1][n-1] == '*'){
        cout << dp[n][n];
        return 0;
    }
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if(i == 1 && j == 1){
                dp[i][j] = 1;
                continue;
            }
            if(s[i-1][j-1] == '*'){
                dp[i][j] = 0;
                continue;
            }
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % mod;
        }
    }
    cout << dp[n][n];
    return 0;
}
