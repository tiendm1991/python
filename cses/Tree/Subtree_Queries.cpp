#include <iostream>
#include <vector>

using namespace std;

const int maxN = 1e5;
bool visited[maxN + 1];
int n, q, a[maxN + 1], de[maxN + 1], ds[maxN + 1], map[maxN + 1], count;
vector<int> adj[maxN + 1];
long long s[maxN + 1], fe[maxN + 1];


void dfs(int u, int p) {
    ds[++count] = u;
    map[u] = count;
    for (int v : adj[u]) {
        if (v == p) {
            continue;
        }
        dfs(v, u);
    }
    de[u] = count;
}

void update(int p, int val) {
    for (int i = p; i <= n; i += i & -i) {
        fe[i] += val;
    }
}

int sum(int p) {
    int ans = 0;
    for (int i = p; i > 0; i -= i & -i) {
        ans += fe[i];
    }
    return ans;
}

int main() {
    cin >> n >> q;
    for (int i = 1; i <= n; i++) {
        cin >> a[i];
    }
    for (int i = 1; i < n; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    dfs(1, 0);
    for (int i = 1; i <= n; i++) {
        update(i, a[ds[i]]);
    }
    for (int i = 0; i < q; i++) {
        int type;
        cin >> type;
        if (type == 1) {
            int s, x;
            cin >> s >> x;
            int idx = map[s];
            update(idx, x - a[idx]);
            a[idx] = x;
        } else {
            int s;
            cin >> s;
            cout << sum(de[s]) - sum(map[s]) << "\n";
        }
    }
    return 0;
}
