#include <iostream>
#include <bits/stdc++.h>

using namespace std;
#define ll long long
const int maxN = 2e5;
int a[maxN];
ll prefix[maxN + 1];
map<ll, int> mp;
int n, x;

int main() {
    cin >> n >> x;
    ll ans = 0;
    mp[0] = 1;
    for (int i = 1; i <= n; i++) {
        cin >> a[i];
        prefix[i] = prefix[i-1] + a[i];
        if(mp.find(prefix[i] - x) != mp.end()){
            ans += mp[prefix[i] - x];
        }
        if (mp.find(prefix[i]) == mp.end()) {
            mp[prefix[i]] = 1;
        } else {
            mp[prefix[i]] += 1;
        }
    }
    cout << ans;
    return 0;
}
