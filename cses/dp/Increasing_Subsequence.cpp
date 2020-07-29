#include <iostream>
#include <bits/stdc++.h>

using namespace std;
#define ll long long
#define arr3 array<int, 3>
const int maxN = 2e5;
int a[maxN];
int n;
int dp[maxN];

int main() {
    cin >> n;
    set<array<int, 2>> s;
    int ans = 1;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        auto it = s.lower_bound({x, 0});
        if (it != s.end()) {
            s.erase(it);
        }
        s.insert({x, i});
    }
    cout << s.size();

}
