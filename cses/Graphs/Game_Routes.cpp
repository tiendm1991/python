#include <iostream>
#include <vector>

using namespace std;
#define ll long long
#define arr2 array<int, 2>

const ll maxN = 1e5, mod = 1e9 + 7;
bool visited[maxN + 1];
vector<int> edges[maxN + 1];
ll d[maxN + 1];
int n, m;

int dfs(int v, int u) {
    if (v == n) {
        d[v] = 1;
        return 0;
    }
    visited[v] = true;
    for (auto i : edges[v]) {
        if (!visited[i]) {
            dfs(i, v);
        }
        d[v] = (d[v] + d[i]) % mod;
    }
    return 0;
}

int main() {
    cin >> n >> m;
    for (int i = 1; i <= m; i++) {
        int a, b;
        cin >> a >> b;
        edges[a].push_back(b);
    }
    dfs(1, 0);
    cout << d[1];
    return 0;
}
