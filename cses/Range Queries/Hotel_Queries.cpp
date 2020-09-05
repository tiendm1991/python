#include <iostream>

using namespace std;
#define ll long long
#define ar array
const int maxN = 2e5;
int a[maxN + 1];
int st[maxN * 4];
int n, q;


void update(int id, int left, int right, int i, int val) {
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
    st[id] = max(st[2 * id + 1], st[2 * id + 2]);
}

int getMax(int id, int left, int right, int u, int v) {
    if (v < left || u > right) {
        return 0;
    }
    if (u <= left && v >= right) {
        return st[id];
    }
    int mid = (left + right) / 2;
    return max(getMax(id * 2 + 1, left, mid, u, v), getMax(id * 2 + 2, mid + 1, right, u, v));
}

int getResult(int id, int left, int right, int x) {
    if (left == right) {
        return left;
    }
    int mid = (left + right) / 2;
    if (st[2 * id + 1] >= x) {
        return getResult(2 * id + 1, left, mid, x);
    } else {
        return getResult(2 * id + 2, mid + 1, right, x);
    }

}

int main() {
    cin >> n >> q;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        update(0, 0, n - 1, i, a[i]);
    }

    for (int i = 0; i < q; i++) {
        int r;
        cin >> r;
        int lb = getMax(0, 0, n - 1, 0, n - 1);
        if (lb < r) {
            cout << "0 ";
        } else {
            int h = getResult(0, 0, n - 1, r);
            cout << h + 1 << " ";
            update(0, 0, n - 1, h, -r);
            a[h] -= r;
        }
    }

}
