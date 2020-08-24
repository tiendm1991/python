// https://www.geeksforgeeks.org/strongly-connected-components/
#include <iostream>
#include <vector>

using namespace std;

const int maxN = 1e5;
int n, m;
vector<int> adj[maxN + 1], adj2[maxN + 1], st, com;
bool visited[maxN + 1], valid[maxN + 1];
int ans[maxN + 1];

void dfs(int u) {
    visited[u] = true;
    for (int v : adj[u]) {
        if (!visited[v]) {
            dfs(v);
        }
    }
    st.push_back(u);
}

void dfs2(int u, int king) {
    visited[u] = false;
    for (int v : adj2[u]) {
        if (visited[v]) {
            dfs2(v, king);
        }
    }
    ans[u] = king;
}

int main() {
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj2[v].push_back(u);
    }
    for (int i = 1; i <= n; i++) {
        if (!visited[i]) {
            dfs(i);
        }
    }
    int k = 0;
    for (int i = n - 1; i >= 0; i--) {
        if (visited[st[i]]) {
            dfs2(st[i], ++k);
        }
    }
    cout << k << "\n";
    for (int i = 1; i <= n; i++) {
        cout << ans[i] << " ";
    }
    return 0;
}
