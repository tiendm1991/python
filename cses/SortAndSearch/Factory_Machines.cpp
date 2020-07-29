#include <iostream>
#include <bits/stdc++.h>

using namespace std;
#define ll long long
const int maxN = 2e5;
int a[maxN];
int n, t;

int main() {
    cin >> n >> t;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    ll l = 1, r = 1e18;
    while (l < r) {
        ll m = (l + r) / 2;
        ll tmp = 0;
        for (int i = 0; i < n; i++) {
            tmp += m / (a[i]);
            if(tmp >= t){
                break;
            }
        }
        if (tmp < t) {
            l = m + 1;
        } else {
            r = m;
        }
    }
    cout << l;

}
