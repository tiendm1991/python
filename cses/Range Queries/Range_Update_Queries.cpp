#include <iostream>

using namespace std;
#define ll long long
#define ar array
const int maxN = 2e5;
ll a[maxN];
struct Node {
    ll lazy; // giá trị T trong phân tích trên
    ll val; // giá trị lớn nhất.
} nodes[maxN * 4];
int n, q;

void down(int id) {
    ll t = nodes[id].lazy;
    nodes[2 * id + 1].lazy += t;
    nodes[2 * id + 1].val += t;
    nodes[2 * id + 2].lazy += t;
    nodes[2 * id + 2].val += t;
    nodes[id].lazy = 0;
}

void update(int id, int left, int right, int u, int v, ll val) {
    if (v < left || u > right) {
        return;
    }
    if (u <= left && right <= v) {
        nodes[id].val += val;
        nodes[id].lazy += val;
        return;
    }
    int mid = (left + right) / 2;
    down(id);
    update(id * 2 + 1, left, mid, u, v, val);
    update(id * 2 + 2, mid + 1, right, u, v, val);
    nodes[id].val = nodes[2 * id + 1].val + nodes[2 * id + 2].val;
}

ll get(int id, int left, int right, int u, int v) {
    if (v < left || u > right) {
        return 0;
    }
    if (u <= left && v >= right) {
        return nodes[id].val;
    }
    int mid = (left + right) / 2;
    down(id);
    return get(id * 2 + 1, left, mid, u, v) + get(id * 2 + 2, mid + 1, right, u, v);
}

int main() {
    cin >> n >> q;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        update(0, 0, n - 1, i, i, a[i]);
    }

    for (int i = 0; i < q; i++) {
        int type;
        cin >> type;
        if (type == 1) {
            ll a, b, u;
            cin >> a >> b >> u;
            update(0, 0, n - 1, a - 1, b - 1, u);
        } else {
            ll k;
            cin >> k;
            cout << get(0, 0, n - 1, k - 1, k - 1) << "\n";
        }
    }

}
