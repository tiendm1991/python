// https://www.geeksforgeeks.org/strongly-connected-components/
#include <iostream>
#include <vector>

using namespace std;

const int maxN = 1e5;
int n, m;
vector<int> adj[maxN + 1], adj2[maxN + 1], st, com;
bool visited[maxN + 1], valid[maxN + 1];

void dfs(int u) {
    visited[u] = true;
    for (int v : adj[u]) {
        if (!visited[v]) {
            dfs(v);
        }
    }
    st.push_back(u);
}

void dfs2(int u) {
    visited[u] = false;
    for (int v : adj2[u]) {
        if (visited[v]) {
            dfs2(v);
        }
    }
    com.push_back(u);
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
    for (int i = n - 1; i >= 0; i--) {
        if (visited[st[i]]) {
            if (com.size() == 0) {
                dfs2(st[i]);
            } else {
                cout << "NO\n";
                cout << st[i] << " " << com[0];
                return 0;
            }
        }
    }
    cout << "YES";
    return 0;
}
