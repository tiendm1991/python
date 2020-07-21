#include <iostream>
#include <bits/stdc++.h>
 
using namespace std;
#define ll long long
#define ar array
const int maxN = 100, maxS = 1e6, mod = 1e9 + 7;
int a[maxN+1];
ll dp[maxS+1];
int n, s;
 
int main() {
    cin >> n >> s;
    for (int i = 0; i < n; i++)
        cin >> a[i];
    dp[0] = 1;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= s; j++) {
            if (j >= a[i - 1]) {
                dp[j] = (dp[j] + dp[j - a[i - 1]]) % mod;
            }
        }
    }
    cout << dp[s];
}
