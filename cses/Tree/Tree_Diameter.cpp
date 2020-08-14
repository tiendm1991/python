#include <iostream>
#include <vector>

using namespace std;
const int maxN = 2e5;
int ans = 0;
bool visited[maxN + 1];
vector<int> adj[maxN + 1];
int n, m;

int dfs(int u) {
    visited[u] = true;
    int d = 0, m1 = 0, m2 = 0;
    for (int v: adj[u]) {
        if (!visited[v]) {
            int x = dfs(v);
            if (x > m1) {
                m2 = m1;
                m1 = x;
            } else if (x > m2) {
                m2 = x;
            }
        }
    }
    d = m1 + m2 +1;
    if (d > ans) {
        ans = d;
    }
    return m1 + 1;
}

int main() {
    cin >> n;
    for (int i = 1; i < n; i++) {
        int a, b;
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    for (int i = 1; i <= n; i++) {
        if (!visited[i]) {
            dfs(i);
        }
    }
    cout << --ans;
    return 0;
}
