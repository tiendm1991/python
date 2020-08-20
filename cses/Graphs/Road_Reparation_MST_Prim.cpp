#include <iostream>
#include <vector>
#include <array>
#include <set>
 
using namespace std;
#define ll long long
#define arr2 array<int, 2>
 
const int maxN = 1e5;
vector<arr2 > edges[maxN + 1];
set<int> mst;
set<arr2 > q;
int p[maxN + 1];
int n, m;
ll ans;
 
int main() {
    cin >> n >> m;
    for (int i = 1; i <= m; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        edges[a].push_back({c, b});
        edges[b].push_back({c, a});
    }
    for (int i = 1; i <= n; i++) {
        p[i] = i;
    }
    q.insert({0, 1});
    while (q.size() > 0 && mst.size() < n) {
        auto it = q.begin();
        int v = (*it)[1];
        if (mst.find(v) == mst.end()) {
            ans += (*it)[0];
            mst.insert(v);
            for (arr2 next: edges[v]) {
                q.insert({next[0], next[1]});
            }
        }
        q.erase(it);
    }
    if (mst.size() < n) {
        cout << "IMPOSSIBLE";
    } else {
        cout << ans;
    }
    return 0;
}
