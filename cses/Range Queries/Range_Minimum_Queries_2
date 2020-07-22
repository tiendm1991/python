#include <iostream>
#include <bits/stdc++.h>

using namespace std;
#define ll long long
#define ar array
const int maxN = 2 * 1e5, maxVal = 1e9;
ll a[maxN];
ll st[4 * maxN + 1];
int n, q;

void update(int id, int left, int right, int i, ll val) {
    if (i < left || i > right) {
        return;
    }
    if (left == right) {
        st[id] = val;
        return;
    }
    int mid = (left + right) / 2;
    update(id * 2 + 1, left, mid, i, val);
    update(id * 2 + 2, mid + 1, right, i, val);
    st[id] = min(st[id * 2 + 1], st[id * 2 + 2]);
}

ll getMin(int id, int left, int right, int u, int v) {
    if (v < left || u > right) {
        return maxVal;
    }
    if (u <= left && v >= right) {
        return st[id];
    }
    int mid = (left + right) / 2;
    return min(getMin(id * 2 + 1, left, mid, u, v), getMin(id * 2 + 2, mid + 1, right, u, v));
}

int main() {
    for (int i = 0; i < 4 * maxN + 1; i++)
        st[i] = maxVal;

    cin >> n >> q;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        update(0, 0, n - 1, i, a[i]);
    }

    int type, x;
    ll y;
    for (int i = 0; i < q; i++) {
        cin >> type >> x >> y;
        if (type == 1) {
            update(0, 0, n - 1, x - 1, y);
            a[x - 1] = y;
        } else {
            cout << getMin(0, 0, n - 1, x - 1, y - 1) << "\n";
        }
    }

}
