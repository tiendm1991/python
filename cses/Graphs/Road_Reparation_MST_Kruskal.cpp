#include <iostream>
#include <vector>
#include <array>
#include <set>
 
using namespace std;
#define ll long long
#define arr3 array<int, 3>
 
const int maxN = 1e5;
set<arr3 > edges;
int p[maxN + 1];
int n, m;
ll ans;
 
int find(int u) {
	if (u != p[u]){
		p[u] = find(p[u]);
	}
    return p[u];
}
 
void unions(int ru, int rv) {
    int r = min(ru, rv), c = max(ru, rv);
    p[c] = r;
}
 
int main() {
    cin >> n >> m;
    for (int i = 1; i <= m; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        edges.insert({c, a, b});
    }
    for (int i = 1; i <= n; i++) {
        p[i] = i;
    }
 
    for (arr3 e: edges) {
        if (n == 1) {
            break;
        }
        int u = e[1], v = e[2], c = e[0];
        int ru = find(u), rv = find(v);
        if (ru != rv) {
            ans += c;
            --n;
            unions(ru, rv);
        }
    }
    if (n > 1) {
        cout << "IMPOSSIBLE";
    } else {
        cout << ans;
    }
    return 0;
}
