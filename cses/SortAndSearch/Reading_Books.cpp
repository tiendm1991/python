#include <iostream>
#include <bits/stdc++.h>

using namespace std;
#define ll long long
const int maxN = 2e5;
int a[maxN];
int n;

int main() {
    cin >> n;
    ll s = 0;
    int m = -maxN;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        s += a[i];
        m = max(m, a[i]);
    }
    
    cout << max(s, 2ll * m);

}
