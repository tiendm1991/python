#include <iostream>
#include <vector>
 
using namespace std;
#define ll long long
#define arr2 array<int, 2>
 
const int maxN = 1e5;
bool visited[maxN + 1];
vector<int> edges[maxN + 1];
int p[maxN + 1], d[maxN + 1];
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
        if (d[i] > 0 && d[i] + 1 > d[v]) {
            d[v] = d[i] + 1;
            p[v] = i;
        }
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
    if (d[1] != 0) {
        vector<int> s;
        int v = 1;
        while (v != n) {
            s.push_back(v);
            v = p[v];
        }
        s.push_back(n);
        cout << s.size() << "\n";
        for (int x : s) {
            cout << x << " ";
        }
    } else {
        cout << "IMPOSSIBLE";
    }
    return 0;
}
