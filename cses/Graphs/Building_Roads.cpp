#include <iostream>
#include <bits/stdc++.h>
 
using namespace std;
#define ll long long
const int maxN = 1e5, maxM = 2e5;
int a[maxN + 1], p[maxN + 1];
int n, m;
 
int root(int x) {
    while (x != p[x]) {
        x = p[x];
    }
    return x;
}
 
void merge(int x, int y) {
    int i = root(x);
    int j = root(y);
    p[max(i, j)] = min(i, j);
}
 
int main() {
    set<array<int, 2>> ans;
    cin >> n >> m;
    for (int i = 1; i <= n; i++) {
        p[i] = i;
    }
    for (int i = 0; i < m; i++) {
        int x, y;
        cin >> x >> y;
        merge(x, y);
    }
    for (int i = 1; i <= n; i++) {
        int r = root(i);
        if (r != 1) {
            ans.insert({1, r});
        }
    }
    cout << ans.size() << "\n";
    for (auto e: ans) {
        cout << e[0] << " " << e[1] << "\n";
    }
    return 0;
}
