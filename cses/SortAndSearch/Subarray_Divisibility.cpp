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
    cin >> n;
    ll ans = 0;
    mp[0] = 1;
    for (int i = 1; i <= n; i++) {
        cin >> a[i];
        if (a[i] >= 0) {
            prefix[i] = (prefix[i - 1] + a[i]) % n;
        } else {
            prefix[i] = (prefix[i - 1] + n - abs(a[i] % n)) % n;
        }
        if (mp.find(prefix[i]) != mp.end()) {
            ans += mp[prefix[i]];
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
