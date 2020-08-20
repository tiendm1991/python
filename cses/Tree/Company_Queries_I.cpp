#include <iostream>
#include <vector>


using namespace std;
const int maxN = 2e5;
bool visited[maxN + 1];
int n, q, a[maxN + 1], tree[maxN + 1][20];
vector<int> adj[maxN + 1];

int dfs(int u) {
    visited[u] = true;
    for (int v : adj[u]) {
        if (visited[v]) {
            continue;
        }
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
    return 0;
}

int main() {
    cin >> n >> q;
    for (int i = 2; i <= n; i++) {
        cin >> a[i];
        adj[i].push_back(a[i]);
        adj[a[i]].push_back(i);
    }
    dfs(1);
    for (int i = 0; i < q; i++) {
        int x, k;
        cin >> x >> k;
        int j = 0;
        while (k > 0) {
            if (k % 2 == 1) {
                x = tree[x][j];
                if (x == 0) {
                    x = -1;
                    break;
                }
            }
            j++;
            k /= 2;
        }
        cout << x << "\n";
    }
    return 0;
}
