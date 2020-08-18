#include <iostream>
#include <vector>
 
 
using namespace std;
const int maxN = 2e5;
bool visited[maxN + 1], visited2[maxN + 1];
vector<int> adj[maxN + 1];
long long n, count[maxN + 1], stSum[maxN + 1];
 
int dfs(int u) {
    visited[u] = true;
    count[u] += 1;
    for (int v: adj[u]) {
        if (!visited[v]) {
            dfs(v);
            count[u] += count[v];
            stSum[u] += stSum[v] + count[v];
        }
    }
    return 0;
}
 
int dfs2(int u) {
    visited2[u] = true;
    for (int v : adj[u]) {
        if (!visited2[v]) {
            stSum[v] = stSum[u] + n - 2 * count[v];
            dfs2(v);
        }
    }
    return 0;
}
 
int main() {
    cin >> n;
    for (int i = 1; i < n; i++) {
        int a, b;
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }
    dfs(1);
    dfs2(1);
    for (int i = 1; i <= n; i++) {
        cout << stSum[i] << " ";
    }
    return 0;
}
