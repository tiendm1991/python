#include <iostream>
#include <bits/stdc++.h>

using namespace std;
#define ll long long
#define arr array<int, 2>
const int maxN = 5000;
ll x[maxN+1], s[maxN+1];
ll dp[maxN+1][maxN+1];
int n;

int main() {
    cin >> n;
    for (int i = 1; i <= n; i++) {
        cin >> x[i];
		s[i] = s[i-1] + x[i];
		
    }
	for(int i = n; i >= 1; i--){
		for(int j = i; j <= n; j++){
			if (i == j){
				dp[i][j] = x[i];
			}else{
				dp[i][j] = (s[j] - s[i-1]) - min(dp[i+1][j], dp[i][j-1]);
			}
		}
	}
    cout << dp[1][n];
    return 0;
}
