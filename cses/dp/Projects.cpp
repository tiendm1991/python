#include <iostream>
#include <bits/stdc++.h>
 
using namespace std;
#define ll long long
#define arr3 array<ll, 3>
#define arr2 array<ll, 2>
 
const int maxN = 2e5;
int n;
arr3 a[maxN+1];
 
int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> a[i][1] >> a[i][0] >> a[i][2];
    }
    sort(a, a+n);
    set<arr2> dp;
    dp.insert({0, 0});
    ll ans = 0;
    for(int i = 0; i < n; i++){
        arr3 p = a[i];
        auto it = dp.lower_bound({p[1], 0});
        --it;
        ll val = (*it)[1] + p[2];
        ans = max(ans, val);
        dp.insert({p[0], ans});
    }
    cout << ans;
}
