#include <iostream>
#include <vector>

using namespace std;

const int maxN = 2e5;
int n, q, a[maxN + 1], order[maxN + 1], pEnd[maxN + 1], pStart[maxN + 1], count;
vector<int> adj[maxN + 1];
long long fe[maxN + 1];


void dfs(int u, int p) {
    order[++count] = u;
    pStart[u] = count;
    for (int v : adj[u]) {
        if (v == p) {
            continue;
        }
        dfs(v, u);
    }
    pEnd[u] = count;
}

void update(int p, int val) {
    for (int i = p; i <= n; i += i & -i) {
        fe[i] += val;
    }
}

long long sum(int p) {
    long long ans = 0;
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
        update(i, a[order[i]]);
        update(pEnd[order[i]] + 1, -a[order[i]]);
    }
    for (int i = 0; i < q; i++) {
        int type;
        cin >> type;
        if (type == 1) {
            int s, x;
            cin >> s >> x;
            int idx = pStart[s];
            update(idx, x - a[s]);
            update(pEnd[s] + 1, a[s] - x);
            a[s] = x;
        } else {
            int s;
            cin >> s;
            cout << sum(pStart[s]) << "\n";
        }
    }
    return 0;
}
