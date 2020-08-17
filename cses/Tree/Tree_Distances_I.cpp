#include <iostream>
#include <vector>
 
using namespace std;
const int maxN = 2e5;
int ans = 0;
bool visited[maxN + 1], isVisited[2][maxN+1];
vector<int> adj[maxN + 1];
int n, v1, v2, p[maxN + 1], dist[2][maxN + 1];
 
int dfs(int u) {
    visited[u] = true;
    int d = 0, m1 = 0, m2 = 0, v1Tmp = 0, v2Tmp = 0;
    for (int v: adj[u]) {
        if (!visited[v]) {
            int x = dfs(v);
            if (x > m1) {
                m2 = m1, m1 = x;
                v2Tmp = v1Tmp, v1Tmp = v;
            } else if (x > m2) {
                m2 = x;
                v2Tmp = v;
            }
        }
    }
    d = m1 + m2 + 1;
    if (d > ans) {
        ans = d;
        v1 = v1Tmp;
        v2 = v2Tmp;
    }
    p[u] = v1Tmp;
    return m1 + 1;
}
 
int dfs2(int u, int d, int idx) {
    isVisited[idx][u] = true;
    dist[idx][u] = d;
    for (int v: adj[u]) {
        if (!isVisited[idx][v]) {
            dfs2(v, d + 1, idx);
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
    while (p[v1] != 0) {
        v1 = p[v1];
    }
    while (p[v2] != 0) {
        v2 = p[v2];
    }
    v1 = max(v1, 1);
    v2 = max(v2, 1);
    for (int i = 1; i < n; i++) {
        visited[i] = false;
    }
    dfs2(v1, 0, 0);
    dfs2(v2, 0, 1);
    for(int i = 1; i <= n; i++){
        cout << max(dist[0][i], dist[1][i]) << " ";
    }
    return 0;
}
