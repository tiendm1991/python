#include <iostream>
#include <bits/stdc++.h>

using namespace std;
#define ll long long
#define ar array
const int maxN = 2 * 1e5;
ll a[maxN];
ll st[4 * maxN + 1];
int n, q;

void update(int id, int left, int right, int i, ll val) {
    if (i < left || i > right) {
        return;
    }
    if (left == right) {
        st[id] += val;
        return;
    }
    int mid = (left + right) / 2;
    update(id * 2 + 1, left, mid, i, val);
    update(id * 2 + 2, mid + 1, right, i, val);
    st[id] = st[id * 2 + 1] + st[id * 2 + 2];
}

ll getSum(int id, int left, int right, int u, int v) {
    if (v < left || u > right) {
        return 0;
    }
    if (u <= left && v >= right) {
        return st[id];
    }
    int mid = (left + right) / 2;
    return getSum(id * 2 + 1, left, mid, u, v) + getSum(id * 2 + 2, mid + 1, right, u, v);
}

int main() {
    for (int i = 0; i < 4 * maxN + 1; i++)
        st[i] = 0;

    cin >> n >> q;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        update(0, 0, n - 1, i, a[i]);
    }

    int type, left;
    ll right;
    for (int i = 0; i < q; i++) {
        cin >> type >> left >> right;
        if (type == 1) {
            update(0, 0, n - 1, left - 1, right - a[left - 1]);
            a[left - 1] = right;
        } else {
            cout << getSum(0, 0, n - 1, left - 1, right - 1) << "\n";
        }
    }

}
