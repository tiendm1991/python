#include <iostream>
#include <vector>
#include <math.h>


using namespace std;
const int maxN = 2e5;
int n, q, a[maxN + 1], tree[maxN + 1][20], h[maxN + 1];

int lca(int u, int v) {
    if (u == v) {
        return u;
    }
    if (h[u] < h[v]) {
        swap(u, v);
    }
    int k = h[u] - h[v];
    int j = 0;
    while (k > 0) {
        if (k % 2 == 1) {
            u = tree[u][j];
        }
        j++;
        k /= 2;
    }
    if (u == v) {
        return u;
    }
    int i = log2(h[u]) + 1;
    while (i >= 0) {
        if (tree[u][i] != tree[v][i]) {
            u = tree[u][i];
            v = tree[v][i];
        }
        i--;
    }

    return a[u];
}

int main() {
    cin >> n >> q;
    for (int i = 2; i <= n; i++) {
        cin >> a[i];
        h[i] = h[a[i]] + 1;
    }
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j < 20; j++) {
            if (j == 0) {
                tree[i][j] = a[i];
            } else {
                if (tree[tree[i][j - 1]][j - 1] == 0) {
                    break;
                } else {
                    tree[i][j] = tree[tree[i][j - 1]][j - 1];
                }
            }
        }
    }
    for (int i = 0; i < q; i++) {
        int x, k;
        cin >> x >> k;
        cout << lca(x, k) << "\n";
    }
    return 0;
}
