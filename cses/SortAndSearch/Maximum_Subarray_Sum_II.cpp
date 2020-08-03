#include <iostream>
#include <bits/stdc++.h>

using namespace std;
#define ll long long
const ll maxN = 2e5, maxV = 1e15;
ll x[maxN + 1], pre[maxN + 1];
ll n, a, b;


int main() {
    cin >> n >> a >> b;
    for (int i = 0; i < n; i++) {
        cin >> x[i];
        pre[i + 1] = pre[i] + x[i];
    }
    ll ans = -maxV;
    set<array<ll, 2>> s;
    for (int i = 0; i <= n; i++) {
        if (i >= a) {
            s.insert({pre[i - a], i - a});
        }
        if (!s.empty()) {
            ans = max(ans, pre[i] - (*s.begin())[0]);
        }
        if (i >= b) {
            s.erase({pre[i - b], i - b});
        }
    }
    cout << ans;
    return 0;
}
