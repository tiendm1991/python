#include <iostream>
#include <vector>
 
using namespace std;
 
const int maxN = 2e5;
int n, dp[2][maxN + 1];
vector<int> adj[maxN + 1];
 
void dfs(int u, int p) {
    vector<int> pre;
    pre.push_back(0);
    for (int v : adj[u]) {
        if (v == p) {
            continue;
        }
        dfs(v, u);
        int maxV = max(dp[0][v], dp[1][v]);
        pre.push_back(maxV);
        // Not choose u
        dp[0][u] += maxV;
    }

    int len = pre.size();
 
    // Calculate choose u
    for (int i = 1, j = 1; i < len; i++, j++) {
        if (adj[u][j - 1] == p) {
            ++j;
        }
        int v = adj[u][j - 1];
        // Choose (u, v)
        dp[1][u] = max(dp[1][u], 1 + dp[0][v] + dp[0][u] - pre[i]);
    }
}
 
int main() {
    cin >> n;
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    dfs(1, 0);
    cout << max(dp[0][1], dp[1][1]);
    return 0;
}
