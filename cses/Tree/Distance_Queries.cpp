#include <iostream>
#include <vector>
#include <math.h>
 
 
using namespace std;
const int maxN = 2e5;
bool visited[maxN + 1];
int n, q, a[maxN + 1], tree[maxN + 1][20], h[maxN + 1];
vector<int> adj[maxN + 1];
 
int dfs(int u) {
    visited[u] = true;
    for (int v : adj[u]) {
        if (visited[v]) {
            continue;
        }
        a[v] = u;
        h[v] = h[u] + 1;
        for (int j = 0; j < 20; j++) {
            if (j == 0) {
                tree[v][j] = a[v];
            } else {
                if (tree[tree[v][j - 1]][j - 1] == 0) {
                    break;
                } else {
                    tree[v][j] = tree[tree[v][j - 1]][j - 1];
                }
            }
        }
        dfs(v);
    }
}
 
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
 
int distance(int u, int v) {
    int l = lca(u, v);
    return h[u] + h[v] - 2 * h[l];
}
 
int main() {
    cin >> n >> q;
    for (int i = 1; i < n; i++) {
        int x, y;
        cin >> x >> y;
        adj[x].push_back(y);
        adj[y].push_back(x);
    }
    dfs(1);
    for (int i = 0; i < q; i++) {
        int x, k;
        cin >> x >> k;
        cout << distance(x, k) << "\n";
    }
    return 0;
}
