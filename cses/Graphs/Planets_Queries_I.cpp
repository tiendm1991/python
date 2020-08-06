#include <iostream>
#include <bits/stdc++.h>

using namespace std;
#define ll long long
#define arr2 array<int, 2>

const int maxN = 2e5;
int n, q, a[30][maxN];

int main() {
    cin >> n >> q;
    for (int i = 0; i < n; i++) {
        cin >> a[0][i];
        --a[0][i];
    }
    for (int i = 1; i < 30; i++) {
        for (int j = 0; j < n; j++) {
            // jump 2*i => x when jump 2 * i-1, jum 2 * i-1
            a[i][j] = a[i - 1][a[i - 1][j]];
        }
    }
    while (q--) {
        int x, k;
        cin >> x >> k;
        --x;
        int c = 0;
        while (k > 0) {
            if (k % 2 == 1) {
                x = a[c][x];
            }
            k /= 2;
            c++;
        }
        cout << x + 1 << "\n";
    }
    return 0;
}
