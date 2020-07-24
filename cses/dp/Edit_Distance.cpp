#include <iostream>
#include <bits/stdc++.h>

using namespace std;
#define ll long long
#define arr array<int, 2>
const int maxN = 5000;
ll dp[maxN + 1][maxN + 1];
string s1, s2;

int main() {
    cin >> s1 >> s2;
    int n1 = s1.length(), n2 = s2.length();
    for (int i = 1; i <= n1; i++) {
        dp[i][0] = i;
    }
    for (int j = 1; j <= n2; j++) {
        dp[0][j] = j;
    }
    for (int i = 1; i <= n1; i++) {
        for (int j = 1; j <= n2; j++) {
            if (s1[i - 1] == s2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1];
            } else {
                dp[i][j] = min(dp[i - 1][j], min(dp[i][j - 1], dp[i - 1][j - 1])) + 1;
            }
        }
    }
    cout << dp[n1][n2];
}
